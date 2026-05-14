---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-43
completeness: full
---

# 43: Streaming Patterns

## Scenario

A company receives large merged PDF files from employees. Each PDF file includes multiple pages with distinct content types, including images and text. The images and text can be categorized into a predefined list. A GenAI developer creates an Amazon Bedrock Data Automation (BDA) project. The GenAI developer uses the BDA project in an AWS Step Functions workflow. The GenAI developer defines custom outputs and provides relevant blueprints as expected. However, the extraction results are inconsistent. The first two pages are correct. However, most of the other pages are missed entirely. Downstream systems receive incomplete metadata. Which combination of steps will resolve this issue with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Enable PDF page splitting in the BDA project.
- Refine the blueprint names and definitions. Include only one blueprint for each content type.

## Common anti-patterns

- Avoid route all PDF files to the image modality. because you can route certain file types to specific modality types by configuring manual modality routing. Routing PDF files to a modality is a way to explicitly map how BDA processes specific content types. Routing all files to...
- Avoid disable all modalities except the text modality. because there are four modalities in BDA: document, image, video, and audio. You can disable a modality for a project if you do not want processing for all types of files. Disabling all modalities except the document...
- Avoid refine the blueprint names and definitions. Provide multiple blueprints of the same content type. because you can refine blueprint names and definitions to improve the accuracy and consistency of document classification. However, providing multiple blueprints of the same...

## Architecture guidance

- Enabling PDF page splitting in the BDA project provides proper processing for multipage PDF files.
- This built-in feature automatically handles page segmentation.
- Therefore, all pages are processed correctly, without requiring additional custom code or services.
