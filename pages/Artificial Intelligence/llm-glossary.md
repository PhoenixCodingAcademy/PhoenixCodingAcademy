# Large Language Models (LLMs) Glossary



# Tokenization

**Tokenization** is the process of breaking down text into smaller units called **tokens** that a language model can process. It's the crucial first step that converts human-readable text into numerical representations that machines can understand.

## The Basic Process

```
"Hello, world!" → ["Hello", ",", "world", "!"] → [15496, 11, 995, 0]
     (text)           (tokens)                    (token IDs)
```

## Types of Tokenization

### 1. **Word-Level**
- Splits by spaces and punctuation
- Simple but creates huge vocabularies
- Example: `"running quickly"` → `["running", "quickly"]`

### 2. **Character-Level**
- Each character is a token
- Very small vocabulary but long sequences
- Example: `"cat"` → `["c", "a", "t"]`

### 3. **Subword-Level** (Most Common in LLMs)
- Balances between words and characters
- Handles unknown words gracefully
- Example: `"unbelievable"` → `["un", "believ", "able"]`

## Why Tokenization Matters

### **Key Functions:**
- **Standardizes input**: Converts variable-length text to fixed vocabulary
- **Handles any text**: Can encode rare words, typos, different languages
- **Enables learning**: Maps text to embeddings the model can process
- **Controls efficiency**: Affects model speed and memory usage

## Modern Tokenization Methods

**BPE (Byte Pair Encoding)**: Used by GPT models
**WordPiece**: Used by BERT
**SentencePiece**: Language-agnostic, used by LLaMA
**Tiktoken**: OpenAI's current tokenizer

Each method learns which text patterns to group together during training, creating an optimal balance between vocabulary size and sequence length.

## Vocabularies

### Special tokens
- **GPT-3/GPT-3 Tokens**.5**: 50,257 tokens  
- **GPT-4**: ~100,000 tokens (estimated)
- **Claude 3**: ~100,000 tokens
- **LLaMA/LLaMA 2**: 32,000 tokens
- **Mistral 7B**: 32,000 tokens
- **BERT**: 30,522 tokens (WordPiece)
- **T5**: 32,128 tokens
- **Command-R**: 256,000 tokens

## Typical Ranges

- **Small vocabularies**: 30,000-50,000 tokens
- **Medium vocabularies**: 50,000-100,000 tokens  
- **Large vocabularies**: 100,000-250,000+ tokens

## Trade-offs

### **Larger Vocabularies**
✅ More efficient encoding (fewer tokens per text)
✅ Better handling of rare words/proper nouns
❌ Larger embedding matrices (more parameters)
❌ Sparser training data per token

When a word not in the tokenization map is encountered, modern tokenizers handle it through **subword tokenization**. Here's what happens:

## Primary Handling Methods

### 1. **Subword Decomposition**
The tokenizer breaks down the unknown word into smaller, known pieces:
- **BPE (Byte Pair Encoding)**: Splits into learned subword units
- **WordPiece**: Similar to BPE, uses prefixes like "##" for continuation
- **SentencePiece**: Can work at the character or byte level

**Example**: "unhappiness" might become → ["un", "happiness"] or ["un", "happ", "iness"]

### 2. **Character-Level Fallback**
If subword units aren't found, the tokenizer falls back to individual characters:
- The word "zxqwy" might become → ["z", "x", "q", "w", "y"]
- Each character typically exists in the vocabulary as a fallback option

### 3. **Byte-Level Encoding**
Some tokenizers (like GPT models) work at the byte level:
- Any UTF-8 string can be represented as bytes
- Guarantees that **any** text can be encoded, no matter how unusual
- Example: Special Unicode characters or emoj




# Sequence
A sequence is a list of tokens. Example: ["un", "happ", "iness", "is", "what", "she", "felt"]# Transformer




# Transformer
The **transformer** is the core architecture that makes modern language models possible.
It is the **underlying neural network structure** that processes text by:
1. Converting words into tokens
2. Processing all tokens simultaneously (not sequentially)
3. Using "attention" to understand relationships between words
4. Generating predictions for the next token

## **Architecture**
A transformer is a **neural network architecture** introduced in 2017. It's a general-purpose design that uses:
- **Self-attention mechanisms** to process sequences in parallel
- **Encoder-decoder structure** (though not always both)
- **Position encodings** to understand sequence order

Think of it as a blueprint or framework that can be used for many tasks.


## **Key Components in LLMs**

### **Self-Attention Mechanism**
The transformer's superpower - it lets the model understand how words relate to each other:
```
"The cat sat on the mat because it was tired"
                                ↑
            [attention looks back to "cat"]
```

### **Layers (Stacked)**
LLMs use many transformer layers (GPT-3 has 96 layers):
- Each layer refines understanding
- Deeper layers capture more complex patterns
- Information flows: tokens → layer 1 → layer 2 → ... → predictions

### **Parallel Processing**
Unlike older models (RNNs), transformers process entire sentences at once:
- **Old way**: Read word → by → word → sequentially
- **Transformer way**: See [all words at once] → understand relationships

## **In Practice**
When you type to ChatGPT:
1. Your text becomes tokens
2. Tokens flow through transformer layers
3. Each layer uses attention to understand context
4. Final layer predicts the most likely next token
5. Repeat until response is complete

The transformer is essentially the "brain architecture" that gives LLMs their intelligence.

## Auto-Regressive Generation

Suppose you ask a transformer "What is a cat?" and that gets tokenized into a sequence: [what, is, a, cat].
That is sent into the tranformer and out comes an "a". Which is appended to the sequence and fed back in iteratively.

```
Step 1: [what, is, a, cat] → Transformer → "a"
Step 2: [what, is, a, cat, a] → Transformer → "cat"  
Step 3: [what, is, a, cat, a, cat] → Transformer → "is"
Step 4: [what, is, a, cat, a, cat, is] → Transformer → "an"
Step 5: [what, is, a, cat, a, cat, is, an] → Transformer → "animal"
```

During this process, if the context window is exceeded, the token at the beginning is removed. This creates a "sliding" window, or circular queue.



## **Key Points About This Process**

### **1. Full Reprocessing**
Each time, the transformer processes the **entire sequence** from scratch:
- It doesn't "remember" previous computations
- Every token gets reprocessed through all layers
- This is why generation can be slow

### **2. Growing Context**
The input keeps growing until either:
- An end token is generated (`<EOS>` or similar)
- The maximum context length is reached
- A stopping criterion is met (like a specific character)

### **3. Why This Seems Inefficient**
You might wonder: "Why reprocess everything?" 

In practice, systems use **KV caching**:
- Stores intermediate computations from previous steps
- Only computes attention for the new token
- Dramatically speeds up generation

## **The Truncation Part**
One small clarification - typically there's no truncation unless you hit the context limit. The sequence just keeps growing:
```
[what, is, a, cat]
[what, is, a, cat, ?]
[what, is, a, cat, ?, A]
[what, is, a, cat, ?, A, cat]
[what, is, a, cat, ?, A, cat, is]
...
```

Only when you exceed the max context length would you need to truncate (remove early tokens).



# Context Window

The number of tokens a transformer can accept is called the **context window** or **context length**, and it varies dramatically:

## **Current Examples**

### **Standard LLMs**
- **GPT-3**: 4,096 tokens
- **GPT-4**: 8,192 tokens (regular) or 32,768 tokens (GPT-4-32k)
- **GPT-4 Turbo**: 128,000 tokens
- **Claude 3**: 200,000 tokens
- **Gemini 1.5 Pro**: 1 million tokens (with up to 10M in research)

### **Open Source Models**
- **LLaMA 2**: 4,096 tokens
- **Mistral**: 8,192 - 32,768 tokens
- **Command R+**: 128,000 tokens

## **What Limits Context Length?**

### **1. Computational Cost**
- Attention mechanism scales **quadratically** O(n²)
- 2x longer sequence = 4x computation
- 10x longer = 100x computation!

### **2. Memory Requirements**
- Must store attention scores for all token pairs
- A 100K context requires ~40GB of GPU memory

### **3. Architecture Design**
- Position encodings must handle the length
- Model must be trained on similar lengths

## **Practical Implications**

```
4K tokens ≈ 3,000 words ≈ 6 pages
8K tokens ≈ 6,000 words ≈ 12 pages  
128K tokens ≈ 96,000 words ≈ 200 pages (a novel)
1M tokens ≈ 750,000 words ≈ 1,500 pages
```

## **The Trend**
Context windows are rapidly expanding through innovations like:
- Sparse attention patterns
- Sliding window attention
- Memory-efficient architectures
- Better position encodings (RoPE, ALiBi)

The limit isn't fixed - it's an engineering challenge being actively solved!







## **LLM = Specific Application**
A Large Language Model (LLM) is a **specific type of model** that:
- **Uses** transformer architecture (usually just the decoder part)
- Is trained on **massive amounts of text data**
- Has **billions of parameters** (GPT-3 has 175B, GPT-4 has ~1.7T)
- Is specifically designed for **language tasks**

An LLM is an application that does the following:
* Input a string.
* Convert it to a sequence by tokenization.
* Repeat:
  * Send sequence into transformer.
  * Get an array of scores (i.e. logits). The array matches the size of the token vocabulary.
  * Use Softmax of the logits and temperature to pick an output token.
  * Append output token to sequence.
  * Remove first token if sequence exceeds the context window.


## **The Relationship**
```
Transformer (broad category)
    ├── LLMs (GPT, Claude, LLaMA)
    ├── Vision Transformers (ViT)
    ├── Audio Transformers (Whisper)
    └── Multimodal Transformers (CLIP, DALL-E)
```

## **Analogy**
- **Transformer** = Like an engine design (can power cars, boats, generators)
- **LLM** = Like a specific sports car using that engine design for racing

Not all transformers are LLMs, but (almost) all modern LLMs are built using transformers.




# Attention

**Attention** is  NLP/machine learning is a mechanism that allows models to assign different weights or importance to different parts of the input when processing information. It determines which words to focus on, but not directly what they mean.

For example, in the sentence "The bank was steep and muddy," an attention mechanism might learn to focus heavily on "steep" and "muddy" when processing "bank" - helping the model recognize this refers to a riverbank, not a financial institution. But the attention mechanism itself is just determining relevance weights; the actual inference of meaning happens through the model's learned representations and subsequent processing.

So attention is more about "what should I pay attention to?" rather than "what does this mean?" - though attention mechanisms certainly help models infer contextual meaning by identifying which surrounding words are most relevant for interpretation.




# Model
A model is a mathematical or computational system that identifies patterns, relationships, or structures in data. Many models learn these patterns through training on example data, then apply what they've learned to make predictions, decisions, or transformations on new data.

See [models](./models.md)

# LLM

An LLM (Large Language Model) is a type of model—that is, a mathematical or computational system—that is trained on massive collections of human language data to identify patterns and structures within natural language. Specifically, LLMs learn from examples during training to enable them to understand, generate, and manipulate text. Using neural network architectures based on transformers, these models can perform a wide range of language tasks, such as answering questions, writing summaries, translating languages, and more.




# Techniques

User: Difference between an LLM and a transformer
Model: Here's the key difference:

## **Transformer = Architecture**
A transformer is a **neural network architecture** introduced in 2017. It's a general-purpose design that uses:
- **Self-attention mechanisms** to process sequences in parallel
- **Encoder-decoder structure** (though not always both)
- **Position encodings** to understand sequence order

Think of it as a blueprint or framework that can be used for many tasks.

## **LLM = Specific Application**
A Large Language Model (LLM) is a **specific type of model** that:
- **Uses** transformer architecture (usually just the decoder part)
- Is trained on **massive amounts of text data**
- Has **billions of parameters** (GPT-3 has 175B, GPT-4 has ~1.7T)
- Is specifically designed for **language tasks**

## **The Relationship**
```
Transformer (broad category)
    ├── LLMs (GPT, Claude, LLaMA)
    ├── Vision Transformers (ViT)
    ├── Audio Transformers (Whisper)
    └── Multimodal Transformers (CLIP, DALL-E)
```

## **Analogy**
- **Transformer** = Like an engine design (can power
User: What is a list of tokens called?
Model: A list of tokens is typically called a **sequence**.

Here are the common terms you'll encounter:

## **Primary Terms**
- **Sequence** - The most common, general term for an ordered list of tokens
- **Token sequence** - More explicit version of the above
- **Input sequence** / **Output sequence** - When referring to what goes into or comes out of a model

## **Context-Specific Terms**
- **Context** - When the tokens are being used as context for prediction
- **Prompt** - The input token sequence given to an LLM
- **Context window** - The maximum sequence length a model can process
- **Tokenized text** - Emphasizes that it came from text

## **In Code**
```python
# You'll often see variable names like:
tokens = [1234, 5678, 910]  # Simple list
input_ids = [1234, 5678, 910]  # Common in libraries like Hugging Face
token_ids = [1234, 5678, 910]  # Alternative naming
```

## **Technical Usage**
- In transformers: "The model processes **sequences** of tokens"
- In training: "Each **sequence** is padded to the same length"
- In papers: "Given an input **sequence** X = (x₁
User: Difference between an LLM and a transformer
Model: Here's the key difference:

## **Transformer = Architecture**
A transformer is a **neural network architecture** introduced in 2017. It's a general-purpose design that uses:
- **Self-attention mechanisms** to process sequences in parallel
- **Encoder-decoder structure** (though not always both)
- **Position encodings** to understand sequence order

Think of it as a blueprint or framework that can be used for many tasks.

## **LLM = Specific Application**
A Large Language Model (LLM) is a **specific type of model** that:
- **Uses** transformer architecture (usually just the decoder part)
- Is trained on **massive amounts of text data**
- Has **billions of parameters** (GPT-3 has 175B, GPT-4 has ~1.7T)
- Is specifically designed for **language tasks**

## **The Relationship**
```
Transformer (broad category)
    ├── LLMs (GPT, Claude, LLaMA)
    ├── Vision Transformers (ViT)
    ├── Audio Transformers (Whisper)
    └── Multimodal Transformers (CLIP, DALL-E)
```

## **Analogy**
- **Transformer** = Like an engine design (can power cars, boats, generators)
- **LLM** = Like a specific sports car using that engine design for racing

Not all transformers are LLMs, but (almost) all modern LLMs are built using transformers.
User: With respect to LLMs, what is a transformer?
Model:  capabilities.In the context of LLMs, a transformer is the **core architecture that makes modern language models possible**. Here's what it does:

## **What It Is**
The transformer is the **underlying neural network structure** that processes text by:
1. Converting words into tokens
2. Processing all tokens simultaneously (not sequentially)
3. Using "attention" to understand relationships between words
4. Generating predictions for the next token

## **Key Components in LLMs**

### **Self-Attention Mechanism**
The transformer's superpower - it lets the model understand how words relate to each other:
```
"The cat sat on the mat because it was tired"
                                    ↑
            [attention looks back to "cat"]
```

### **Layers (Stacked)**
LLMs use many transformer layers (GPT-3 has 96 layers):
- Each layer refines understanding
- Deeper layers capture more complex patterns
- Information flows: tokens → layer 1 → layer 2 → ... → predictions

### **Parallel Processing**
Unlike older models (RNNs), transformers process entire sentences at once:
- **Old way**: Read word → by → word → sequentially
- **Transformer way**: See [all words at once] → understand relationships

## **In Practice**
When you type to ChatGPT:
1. Your text becomes tokens
2. Tokens flow through transformer layers
3. Each layer uses attention to understand context
4. Final layer predicts the most likely next token
5. Repeat until response is complete

The transformer is essentially the "brain architecture" that gives LLMs their intelligence.
User: Do the tokens flow into a transformer one at a time?
Model: **No**, tokens flow into a transformer **all at once** (in parallel), not one at a time. This is one of the transformer's key innovations.

## **How Tokens Actually Flow**

### **During Processing**
```
Input: "The cat sat on the mat"
         ↓
Tokens: [The] [cat] [sat] [on] [the] [mat]
         ↓
    ALL ENTER TRANSFORMER SIMULTANEOUSLY
         ↓
    Process in parallel through layers
```

### **During Generation** 
This is where it gets interesting - there's a distinction:

1. **Initial prompt**: All tokens enter at once
   ```
   "Write a poem about" → [Write] [a] [poem] [about] 
                           ↓ ALL AT ONCE ↓
   ```

2. **Generating new tokens**: One at a time output
   ```
   Step 1: [Write] [a] [poem] [about] → predicts [flowers]
   Step 2: [Write] [a] [poem] [about] [flowers] → predicts [in]
   Step 3: [Write] [a] [poem] [about] [flowers] [in] → predicts [spring]
   ```

## **The Key Insight**
- **Processing**: Parallel (all tokens at once)
- **Generation**: Sequential (one new token at a time)
- **But**: Each generation step processes ALL previous tokens in parallel

This parallel processing is why transformers are:
- Much faster than older sequential models
- Better at understanding long-range dependencies
- Able to "see" the full context when making predictions
User: How many tokens can go into a transformer
Model: The number of tokens a transformer can accept is called the **context window** or **context length**, and it varies dramatically:

## **Current Examples**

### **Standard LLMs**
- **GPT-3**: 4,096 tokens
- **GPT-4**: 8,192 tokens (regular) or 32,768 tokens (GPT-4-32k)
- **GPT-4 Turbo**: 128,000 tokens
- **Claude 3**: 200,000 tokens
- **Gemini 1.5 Pro**: 1 million tokens (with up to 10M in research)

### **Open Source Models**
- **LLaMA 2**: 4,096 tokens
- **Mistral**: 8,192 - 32,768 tokens
- **Command R+**: 128,000 tokens

## **What Limits Context Length?**

### **1. Computational Cost**
- Attention mechanism scales **quadratically** O(n²)
- 2x longer sequence = 4x computation
- 10x longer = 100x computation!

### **2. Memory Requirements**
- Must store attention scores for all token pairs
- A 100K context requires ~40GB of GPU memory

### **3. Architecture Design**
- Position encodings must handle the length
- Model must be trained on similar lengths

## **Practical Implications**

```
4K tokens ≈ 3,000 words ≈ 6 pages
8K tokens ≈ 6,000 words ≈ 12 pages  
128K tokens ≈ 96,000 words ≈ 200 pages (a novel)
1M tokens ≈ 750,000 words ≈ 1,500 pages
```

## **The Trend**
Context windows are rapidly expanding through innovations like:
- Sparse attention patterns
- Sliding window attention
- Memory-efficient architectures
- Better position encodings (RoPE, ALiBi)

The limit isn't fixed - it's an engineering challenge being actively solved!




## **1. Tokenizer**
**Before** the transformer:
```
"What is a cat?" 
    ↓ Tokenizer
[1234, 567, 89, 2345, 99]  (token IDs)
```
- Converts text → token IDs
- Has a vocabulary (e.g., 50,000 tokens)
- Handles special tokens (`<BOS>`, `<EOS>`, `<PAD>`)

## **2. Embedding Layer**
**First layer** that tokens hit:
```
Token ID: 1234
    ↓ Embedding
Vector: [0.23, -1.45, 0.89, ...] (e.g., 4096 dimensions)
```
- Converts token IDs → dense vectors
- Learned during training
- Captures semantic meaning

## **3. Output Head (LM Head)**
**After** the transformer:
```
Final transformer layer: [hidden states]
    ↓ Linear projection
Logits: [score for token 1, score for token 2, ..., score for token 50000]
```
- Projects hidden states → vocabulary size
- Produces a score for every possible next token

## **4. Sampling/Decoding Strategy**
**Chooses** which token to output:
```
Logits: [2.1, 0.3, 5.7, -1.2, ...]
    ↓ Softmax → Probabilities
    ↓ Sampling method
Selected token: 2345
```
Methods include:
- **Greedy**: Pick highest probability
- **Temperature sampling**: Add randomness
- **Top-k/Top-p**: Sample from likely candidates
- **Beam search**: Track multiple possibilities

## **5. Positional Encoding**
**Added** to embeddings:
```
Token embedding + Position encoding = Input to transformer
[cat vector] + [position 3 vector] = Final input
```
- Tells the model where tokens are in sequence
- Can be learned or fixed (sinusoidal)

## **The Full Pipeline**
```
"What is a cat?"
    ↓ Tokenizer
[1234, 567, 89, 2345, 99]
    ↓ Embedding Layer
[[0.23, -1.45, ...], [0.67, 0.89, ...], ...]
    ↓ + Positional Encoding
[[0.25, -1.43, ...], [0.70, 0.91, ...], ...]
    ↓ TRANSFORMER LAYERS (the part you mentioned)
[[hidden states], ...]
    ↓ LM Head
[logits for all 50K tokens]
    ↓ Sampling
Token 4567 ("A")
    ↓ Detokenizer
"A"
```

The transformer is the "brain," but these components are the full "nervous system" that makes text in/out possible!
User: When a sequence is put into the transformer, is the output a set of tokens with probabilities associated with each token?
Model: **Almost, but not quite!** The transformer outputs something that gets converted to probabilities. Here's what actually happens:

## **What Actually Comes Out**

The transformer outputs **logits** (raw scores), not probabilities:

```
Input: [What, is, a, cat]
          ↓ Transformer
Output: Logits for next token position
        [2.1, -0.5, 4.3, -2.0, 1.5, ...]  ← one score per vocabulary token
         "the" "dog" "?" "xyz" "A"
```

## **Converting to Probabilities**

These logits then go through **softmax** to become probabilities:

```
Logits: [2.1, -0.5, 4.3, -2.0, 1.5, ...]
           ↓ Softmax
Probs:  [0.15, 0.01, 0.73, 0.002, 0.08, ...]
         "the" "dog" "?"  "xyz"  "A"
         
(These sum to 1.0)
```

## **Important Detail: One Position Only**

The transformer predicts **only the next token**, not multiple tokens:

```
[What, is, a, cat] → predicts token 5 only
[What, is, a, cat, ?] → predicts token 6 only
```

## **During Training vs Inference**

### **Training** (Teacher Forcing)
Actually predicts at ALL positions simultaneously:
```
Input:  [What, is, a, cat]
Output: [logits for pos 2] [logits for pos 3] [logits for pos 4] [logits for pos 5]
         (predicting "is")  (predicting "a")   (predicting "cat") (predicting "?")
```

### **Inference** (Generation)
Only uses the last position:
```
Input:  [What, is, a, cat]
Output: [ignored] [ignored] [ignored] [logits for next token]
```

## **The Full Picture**
```
Transformer output: [-1.2, 3.4, 0.5, ...] (50,000 logits)
                          ↓
                      Softmax
                          ↓
                    [0.002, 0.73, 0.05, ...] (50,000 probabilities)
                          ↓
                    Sample/Select
                          ↓
                    Token ID: 1234
```

So yes, you get probabilities for each possible token, but only after converting the raw logits!
User: If the token vocabulary is 50,000 tokens, does that mean that the tranformer has 50,000 outputs
Model: **Yes, exactly!** The transformer (specifically the LM head after the transformer layers) has 50,000 outputs - one for each token in the vocabulary.

## **The Output Structure**

```
Final transformer layer: [hidden state vector] (e.g., 4096 dimensions)
                              ↓
                          LM Head 
                    (Linear projection)
                              ↓
                    [50,000 outputs]
                    
Output[0] = score for token "the"
Output[1] = score for token "a"  
Output[2] = score for token "dog"
...
Output[49,999] = score for token "<EOS>"
```

## **Concrete Example**

If your vocabulary is:
```
{0: "the", 1: "cat", 2: "is", 3: "what", ..., 49999: "<END>"}
```

Then output looks like:
```
[2.3, -1.5, 4.7, 0.2, ..., -0.8]
  ↑    ↑    ↑    ↑         ↑
"the" "cat" "is" "what"  "<END>"
```

## **Why So Many?**

The model needs to be able to predict **any token** in its vocabulary as the next token:
- Common words: "the", "is", "and"
- Rare words: "antidisestablishmentarianism"
- Subwords: "##ing", "##tion"
- Special tokens: `<EOS>`, `<PAD>`, `<UNK>`
- Punctuation: ".", "?", "!"
- Even individual characters or bytes sometimes

## **The Computational Cost**

This is actually a bottleneck:
```
Hidden size: 4,096
Vocabulary: 50,000
LM Head matrix: 4,096 × 50,000 = 204.8 million parameters!
```

For GPT-3 (hidden size 12,288):
```
12,288 × 50,257 = 617.5 million parameters just for output layer!
```

## **Memory Efficient Alternatives**

Some models use tricks to reduce this:
- **Weight tying**: Share embeddings with output layer
- **Adaptive softmax**: Use different sizes for common vs rare tokens
- **Mixture of Experts**: Only compute a subset of outputs

But yes, fundamentally, the model outputs one score for every possible token it knows!
User: When does an LLM know when to stop generating an output?
Model: Great question! LLMs can stop generating output in several ways:




## **1. End-of-Sequence Token**

The most common method - the model generates a special token:
```
"What is a cat?"
↓
"A cat is an animal." <EOS>
                       ↑ Model generates this
```
When the model outputs `<EOS>` (or `</s>`, `<|endoftext|>`, etc.), generation stops.

## **2. Maximum Length Reached**

A hard limit prevents infinite generation:
```python
max_tokens = 100
if len(generated_tokens) >= max_tokens:
    stop()
```
- GPT models often default to 2048 or 4096 tokens
- You can usually configure this

## **3. Stop Sequences**

User-defined strings that trigger stopping:
```python
stop_sequences = ["\n\n", "Question:", "END"]

"Here's the answer: A cat is an animal.\n\nQuestion:"
                                          ↑ Stops here
```

## **4. Probability/Confidence Threshold**

Stop if the model becomes too uncertain:
```
Token probabilities: [0.9, 0.8, 0.7, 0.3, 0.1, 0.05...]
                                         ↑ Too uncertain, stop
```

The model doesn't "know" it should stop - it just predicts tokens, and eventually predicts a stop token (or we force it to stop)!



# Chain of Thought (CoT)
A CoT LLM model is a transformer that has been training with millions of examples where:
- "Step by step" appeared before detailed explanations
- Math textbooks showed worked solutions with intermediate steps
- Educational content broke down complex problems into parts
- People explaining their reasoning would naturally say things like "let me work through this step by step"

So when you prompt with "Let's think step by step" you're essentially activating those patterns. The model has learned that this phrase is typically followed by:
1. Breaking down the problem
2. Showing intermediate calculations
3. Explaining logic clearly
4. Arriving at a conclusion

You could achieve similar effects with other phrases like:
- "Let's work through this carefully"
- "First, let me break this down"
- "Let's solve this methodically"
- "Thinking through this problem:"

The key is that "step by step" reliably triggers the generation pattern of incremental reasoning rather than jumping straight to an answer. Without it, the model might just output "11" directly. With it, the model generates the intermediate reasoning, and crucially, those intermediate tokens become part of the context that helps it arrive at the correct final answer.

It's a bit like how asking a student to "show your work" gets different results than just asking for the answer!




# Mixture of Experts (MoE)
A "Mixture of Experts" (or MoE) is a single model that has different pathways in its neural network that act as experts.
Imagine a system of one or more LLMs where the output of one LLM might become the input to one or more other LLMs.
Each LLM is a specialist in some area, like health, physics, math, etc.
The initial text input likely goes to one LLM (a dispatcher) that decides which parts of the text are suitable to send to other expert LLMs.
The output of these experts are then coalesced into a final answer.
Put this into one model and you get a MoE.

In a typical neural network, each neuron in a layer is typically connected to every neuron in the next layer.
In a MoE, this would not be the case. Perhaps the first layer might be a gating layer that determines which network to send it to.
* Expert 1 might be neurons 1-1000
* Expert 2 might be neurons 1001-2000
* etc.



# Agentic Systems
An agentic is a system of one or more agents, where each agent is an LLM that perceives, decides, or acts.
Although perceive, decide, and act basically mean input, process, and output; the distinction is:
* Perceive means input from the environment or another agent.
* Decide means process.
* Act means output to the environment or another agent.
An agentic system has at least one agent inputting data from the environment, and at least one agent outputting data to the environment.


