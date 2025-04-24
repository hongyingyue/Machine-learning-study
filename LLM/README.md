


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
