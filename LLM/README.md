
# Tokenizor
- Word based
- Character based
- Subword tokenization
  - WordPiece, as used in BERT
  - Byte-level BPE, as used in GPT-2
  - SentencePiece or Unigram, as used in several multilingual models

# Model

## Llama
Developed by Meta.

[The Llama 3 Herd of Models](https://arxiv.org/pdf/2407.21783)

## BERT Family

### 🔧 **RoBERTa** (Robustly Optimized BERT Approach)
Developed by Facebook AI.

**Main Improvements:**
1. **More Training Data**  
   - Uses **160GB** of text (vs. BERT’s 16GB).
2. **Longer Training Time**  
   - Trained longer, with **larger batches and more steps**.
3. **No Next Sentence Prediction (NSP)**  
   - Removed NSP to improve training efficiency.
4. **Dynamic Masking**  
   - Applies masking **during training** rather than once at the start like BERT.

**Effect:**  RoBERTa is essentially a better-trained BERT, achieving **higher accuracy across many benchmarks**.

---

### 🔧 **DeBERTa** (Decoding-enhanced BERT with Disentangled Attention)
Developed by Microsoft.

**Main Innovations:**
1. **Disentangled Attention Mechanism**  
   - Separates word **content** and **position** into two embeddings and processes them **independently**, then combines using a new attention mechanism.
2. **Enhanced Position Encoding**  
   - Relative position encoding is more context-aware than BERT’s absolute position.
3. **Decoder-Style Architecture (DeBERTa v2+)**  
   - Uses **both encoder and decoder innovations** for even better performance.

**Effect:**  DeBERTa outperforms RoBERTa and BERT on many benchmarks (e.g., GLUE, SuperGLUE) with **fewer parameters or similar compute**.

---

### 🧠 Summary Table:

| Model     | Key Upgrade                     | Performance Gain |
|-----------|----------------------------------|------------------|
| **RoBERTa** | More data + dynamic masking       | More robust than BERT |
| **DeBERTa** | Disentangled attention + better position encoding | Outperforms RoBERTa |

## Others
- Models have different supported sequence lengths, and some specialize in handling very long sequences. **Longformer** is one example, and another is **LED**.


# Evaluation

## [GLUE](https://gluebenchmark.com/)
The General Language Understanding Evaluation (GLUE) benchmark is a collection of resources for training, evaluating, and analyzing natural language understanding systems.