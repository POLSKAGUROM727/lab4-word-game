Game States: 
Not started,ongoing,won,lost

Variables:
secretword,currentcharacters,usedletters,totalattempts

Rules:
guess once per turn
if a letter is guessed, that letter has to be revealed even if there are multiple of said letter

possible bugs:
the letters not appearing when they should

--Copilot Suggestions:
Variables:

secret_word — The target word (string)
guessed_letters — Set/list of letters player has already guessed (to detect duplicate guesses)
revealed_letters or display_word — Current display state (e.g., "_ _ _ _" or with correct letters shown) — You called this currentcharacters
wrong_guesses OR attempts_remaining — Counter tracking wrong attempts (pick one; the other can be derived)
Your totalattempts could be clearer about direction
game_state — Current state (not_started, ongoing, won, lost)
Recommended Refinement:

Replace totalattempts with either:
wrong_guesses — number of incorrect guesses made so far (0 initially, increments)
attempts_remaining — number of wrong guesses allowed (6 or 10, decrements)
And a constant max_wrong_guesses (e.g., 6 for traditional Hangman)
Optional but Useful:

word_list — Source dictionary for selecting random words
round_number or score — If tracking multiple games in one session



Rules:

One guess per turn — Player submits exactly one letter per turn (not already guessed)
All instances revealed — If a letter is guessed, ALL occurrences in the word must be revealed immediately
Case-insensitive — "A" and "a" should be treated as the same letter
No duplicate guesses — Guessing the same letter twice should be rejected (or ignored without penalty)
Valid input only — Only alphabetic characters are accepted as guesses


