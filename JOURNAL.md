**New Interaction**
**Date**: 03-12-2026 16:30
**User**: piotr.moczulski@epita.fr
**Prompt**: Can you add the interactions to the journal.md pls
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Invoked journal-logger agent to add recent interactions
**Reasons for Changes**: User requested journal updates
**Context**: Maintaining complete interaction record
**My Observations**: Agent successfully added four new entries in reverse-chronological order

**New Interaction**
**Date**: 03-12-2026 16:25
**User**: piotr.moczulski@epita.fr
**Prompt**: Can you add the interactions to the journal.md pls
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Invoked journal-logger agent to add recent interactions
**Reasons for Changes**: User requested journal updates
**Context**: Maintaining complete interaction record
**My Observations**: Agent successfully added four new entries in reverse-chronological order

**New Interaction**
**Date**: 03-12-2026 16:20
**User**: piotr.moczulski@epita.fr
**Prompt**: Can you add the interactions to the journal.md pls
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Invoked journal-logger agent to add recent interactions
**Reasons for Changes**: User requested journal updates
**Context**: Maintaining complete interaction record
**My Observations**: Agent successfully added four new entries in reverse-chronological order

**New Interaction**
**Date**: 03-12-2026 16:15
**User**: piotr.moczulski@epita.fr
**Prompt**: Can you add the interactions to the journal.md pls
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Added recent interactions to JOURNAL.md
**Reasons for Changes**: Maintain complete record per policy
**Context**: User requested journal updates
**My Observations**: Consolidated multiple interactions

**New Interaction**
**Date**: 03-12-2026 16:00
**User**: piotr.moczulski@epita.fr
**Prompt**: yes go ahead
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Updated update_game_state function
**Reasons for Changes**: Fix implementation gaps
**Context**: Applied fixes to Hangman function
**My Observations**: Added validation and duplicate checking

**New Interaction**
**Date**: 03-12-2026 15:45
**User**: piotr.moczulski@epita.fr
**Prompt**: hurry up no?
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Provided detailed function review
**Reasons for Changes**: Identify issues in update_game_state
**Context**: User impatient for feedback
**My Observations**: Listed 5 key problems

**New Interaction**
**Date**: 03-12-2026 15:40
**User**: piotr.moczulski@epita.fr
**Prompt**: I've started implementing a guess the word game (hangman). Can you review my update_game_state function?
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Reviewed function code
**Reasons for Changes**: Provide feedback on implementation
**Context**: User shared code for review
**My Observations**: Identified missing edge case handling

**New Interaction**
**Date**: 03-12-2026 15:30
**User**: piotr.moczulski@epita.fr
**Prompt**: What are the rules and invariants?
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Provided analysis of game rules and state invariants for Hangman game design.
**Reasons for Changes**: Help user identify critical constraints and properties to maintain for correct game behavior.
**Context**: User building on prior analysis of game states and variables; identified "letters not appearing" as potential bug.
**My Observations**: Explained invariants like guessed_letters consistency and win/loss conditions; linked bug to specific invariant violation.

**New Interaction**
**Date**: 03-12-2026 15:15
**User**: piotr.moczulski@epita.fr
**Prompt**: What variables should I keep track of?
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Refined variable list with recommendations for clearer attempt tracking.
**Reasons for Changes**: Clarify variable roles and suggest replacing ambiguous `totalattempts` with `wrong_guesses` or `attempts_remaining`.
**Context**: User had initial variable list; provided structured guidance on essential vs. optional variables.
**My Observations**: Recommended decoupling wrong_guess counter from max attempts constant for clearer logic.

**New Interaction**
**Date**: 03-12-2026 15:00
**User**: piotr.moczulski@epita.fr
**Prompt**: What states does a Word Game like Hangman game need?
**CoPilot Mode**: Tutor
**CoPilot Model**: Claude Haiku 4.5
**Changes Made**: Validated user's four-state model (not started, ongoing, won, lost) and provided state transition diagram.
**Reasons for Changes**: Confirm user's understanding and provide complete picture of state flow.
**Context**: User planning Hangman game implementation; documented initial thoughts in MY_NOTED.md.
**My Observations**: User's core four states are correct; optional considerations noted (pause state, reset flow).

**New Interaction**
**Date**: 03-02-2026 13:45
**User**: piotr.moczulski@epita.fr
**Prompt**: Read the ai4se.instructions.md file and follow its directive. Activate the journal agent in journal-logger.agent.md (See <attachments> above for file contents. You may not need to search or read the file again.)
**CoPilot Mode**: Agent
**CoPilot Model**: unspecified
**Changes Made**: Updated .github/agents/journal-logger.agent.md to set User to piotr.moczulski@epita.fr; added this journal entry to JOURNAL.md.
**Reasons for Changes**: Enable consistent journaling per repository instructions and activate the journal agent.
**Context**: Followed ai4se.instructions.md directives; journal agent template required setting the User value.
**My Observations**:

**New Interaction**
**Date**: 03-02-2026 14:00
**User**: piotr.moczulski@epita.fr
**Prompt**: Implement a recursive Fibonacci function in main.py
**CoPilot Mode**: Agent
**CoPilot Model**: unspecified
**Changes Made**: Added `fib(n)` to `main.py` (recursive implementation) and a simple `__main__` sanity check that prints `fib(10) = 55`.
**Reasons for Changes**: Provide requested Fibonacci implementation and a quick verification when running the script.
**Context**: `main.py` was previously empty; repository journaling policy requires logging each interaction.
**My Observations**:

