from datasets import load_dataset
from torch.utils.data import Dataset
import torch
from sklearn.model_selection import train_test_split
from torch.nn.utils.rnn import pad_sequence

def tokenize(text):
    # split the sentence by space and make them lower cases
    return text.lower().split()

class IMDbDataset(Dataset):
    def __init__(self, texts, labels, vocab):
        self.texts = [torch.tensor([vocab.get(token, vocab["<UNK>"]) for token in tokenize(t)]) for t in texts]
        self.labels = torch.tensor(labels)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.texts[idx], self.labels[idx]

def build_vocab(texts, max_vocab_size=10000):
    from collections import Counter
    counter = Counter(token for text in texts for token in tokenize(text))
    most_common = counter.most_common(max_vocab_size - 2)
    vocab = {"<PAD>": 0, "<UNK>": 1}
    vocab.update({word: idx + 2 for idx, (word, _) in enumerate(most_common)})
    return vocab

def collate_fn(batch):
    texts, labels = zip(*batch)
    padded = pad_sequence(texts, batch_first=True, padding_value=0)
    return padded, torch.tensor(labels)

def get_dataloaders(batch_size=16):
    dataset = load_dataset("imdb", split="train[:500]")
    texts, labels = dataset["text"], dataset["label"]

    X_train, X_val, y_train, y_val = train_test_split(texts, labels, test_size=0.2)
    vocab = build_vocab(X_train)

    train_ds = IMDbDataset(X_train, y_train, vocab)
    val_ds = IMDbDataset(X_val, y_val, vocab)

    train_loader = torch.utils.data.DataLoader(train_ds, batch_size=batch_size, collate_fn=collate_fn)
    val_loader = torch.utils.data.DataLoader(val_ds, batch_size=batch_size, collate_fn=collate_fn)

    return train_loader, val_loader, vocab