---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-21
completeness: full
---

# 21: Implementation Patterns

## Scenario

A company is developing a product description generator by using Amazon Bedrock. The generator must provide creative but controlled product descriptions between 50–100 words. The descriptions must maintain consistency with brand guidelines but provide some variation in style. The company needs to optimize the model's output parameters to achieve the desired balance. Which configuration will meet these requirements?

## Common implementation patterns

- Set the temperature to 0.5. Set top-p to 0.8. Configure length penalties for responses that exceed brand guidelines.

## Common anti-patterns

- Avoid set the temperature to 0.2. Set top-k to 4. Configure strict stop sequences for brand-specific terms. because temperature controls randomness in token selection. A lower temperature produces a more deterministic output. A temperature of 0.2 combined with a top-k of 4...
- Avoid set the temperature to 0.5. Configure response length limits. Disable all diversity parameters. because a mid-range temperature balances determinism and randomness. You can disable the diversity parameters top-p or top-k to apply strict length limits. This configuration...
- Avoid set the temperature to 0.9. Set top-k to 50. Remove all response length limitations. because high temperature and large top-k maximizes randomness and creativity. This configuration removes response limits and allows unconstrained text generation. This configuration...

## Architecture guidance

- Temperature controls randomness in token selection.
- A higher temperature increases variability for creative output.
- Top-p (nucleus sampling) selects tokens from the most likely subset to balance diversity and coherence.
