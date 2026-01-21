from .prompt_combinator import PromptCombinator
from .prompt_combinator import PromptCombinatorMerger
from .prompt_combinator import PromptCombinatorExportGallery
from .prompt_combinator import PromptCombinatorRandomPrompt
from .prompt_combinator import PromptCombinatorRandomPrompts

NODE_CLASS_MAPPINGS = {
    "PromptCombinator": PromptCombinator,
    "PromptCombinatorMerger": PromptCombinatorMerger,
    "PromptCombinatorExportGallery": PromptCombinatorExportGallery,
    "PromptCombinatorRandomPrompt": PromptCombinatorRandomPrompt,
    "PromptCombinatorRandomPrompts": PromptCombinatorRandomPrompts,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptCombinator": "🔢 Prompt Combinator",
    "PromptCombinatorMerger": "🔢 Prompt Combinator Merger",
    "PromptCombinatorExportGallery": "🔢 Prompt Combinator Export Gallery",
    "PromptCombinatorRandomPrompt": "🔢 Pick Random Prompt from Prompt Combinator",
    "PromptCombinatorRandomPrompts": "🔢 Pick Random Prompts from Prompt Combinator",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
