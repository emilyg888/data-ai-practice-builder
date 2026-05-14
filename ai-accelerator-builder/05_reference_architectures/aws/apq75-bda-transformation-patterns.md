---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-75
completeness: full
---

# 75: BDA Transformation Patterns

## Scenario

A company is building a contract analysis system by using intelligent document processing capabilities in Amazon Bedrock. The system uses a blueprint to extract fields, such as AuthorizedSigner, from legal agreements. An example of an extracted value is Mr. John Allen Doe III, Senior Legal Counsel. The company needs to split the fields into the following individual components: TITLE, FIRST_NAME, MIDDLE_NAME, LAST_NAME, SUFFIX, and JOB_TITLE. The company will reuse the structured name format across multiple extracted fields including AuthorizedSigner, WitnessName, and ReviewerName in the pipeline. Which Bedrock Data Automation (BDA) capability will meet these requirements?

## Common implementation patterns

- Use transformation with a reusable custom type to split the AuthorizedSigner field into subcomponents.

## Common anti-patterns

- Avoid use extraction to map subfields directly from text by assigning aliases. because extraction retrieves field values. However, extraction does not parse or split complex text strings such as names with titles and suffixes. Aliases can rename fields but not split fields.
- Avoid use normalization to parse and split the value using pattern-based replacements. because normalization standardizes field formats. For example, normalization can convert "NY" to "New York". Normalization does not support semantic splitting or creating structured field...
- Avoid use validation to enforce required subfields, such as FIRST_NAME and LAST_NAME, and to reject malformed names. because validation helps enforce constraints after transformation. For example, validation can check for null values or incorrect formats. However, validation...

## Architecture guidance

- Transformation can split complex fields into structured components.
- For example, transformation can split full names.
- You can use a custom type to define and reuse this structure across fields such as AuthorizedSigner or ReviewerName.
