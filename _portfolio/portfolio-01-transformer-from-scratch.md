---
title: "GPT-2 From Scratch: A First-Principles Transformer"
excerpt: "LLM · Transformers · PyTorch<br/><img src='/images/transformer_from_scratch.webp' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** LLM · Transformers · PyTorch

A from-scratch implementation of a GPT-2 style transformer in PyTorch, built up one component at a time to understand the architecture from first principles rather than calling into a library. Each block is implemented by hand and tested against a reference GPT-2 (via TransformerLens) to confirm the activations match:

- **LayerNorm** — normalization with learned scale and bias
- **Token & positional embeddings** — lookup tables mapping tokens and positions into the residual stream
- **Multi-head self-attention** — Q/K/V projections, masked attention scores, and per-head mixing
- **MLP / feed-forward** block with GELU
- **Transformer block** — residual connections wiring attention and MLP together
- **Unembedding** to logits, assembled into the **full transformer**

A small training loop then trains the model end-to-end on text, demonstrating next-token prediction on the architecture built above.

Built while following Neel Nanda's transformer implementation tutorial.

[Colab notebook](https://drive.google.com/file/d/1Exn79AxPeW_E-NHRFYquS0YgtaVMBSkP/view?usp=sharing) · 
[Reference video](https://www.youtube.com/watch?v=dsjUDacBw8o&t=3013s)