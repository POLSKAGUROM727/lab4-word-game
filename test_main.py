import pytest

from main import update_game_state, build_display_word, check_win_condition, Game


@pytest.mark.parametrize("secret,guesses,guess,lives,expected", [
    ("apple", [], "a", 6, (["a"], 6)),
    ("apple", ["a"], "p", 6, (["a", "p"], 6)),
    ("apple", ["a"], "x", 6, (["a", "x"], 5)),
    ("Banana", [], "b", 3, (["b"], 3)),  # case insensitivity
])
def test_update_game_state_regular(secret, guesses, guess, lives, expected):
    assert update_game_state(secret, guesses, guess, lives) == expected


def test_duplicate_guess_has_no_effect():
    guessed = ["a", "b"]
    lives = 4
    result = update_game_state("cat", guessed, "A", lives)
    assert result == (guessed, lives)


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        update_game_state("word", [], "ab", 5)
    with pytest.raises(ValueError):
        update_game_state("word", [], "1", 5)
    with pytest.raises(ValueError):
        update_game_state("word", [], "", 5)


@pytest.mark.parametrize("secret,guessed,expected", [
    ("cat", [], "_ _ _"),
    ("cat", ["c"], "c _ _"),
    ("cat", ["c", "a"], "c a _"),
    ("cat", ["c", "a", "t"], "c a t"),
    ("Python", ["p", "o"], "p _ _ _ o _"),
])
def test_build_display_word(secret, guessed, expected):
    assert build_display_word(secret, guessed) == expected


@pytest.mark.parametrize("secret,guessed,expected", [
    ("cat", ["c", "a", "t"], True),
    ("cat", ["c", "a"], False),
    ("python", ["p", "y", "t", "o", "n"], False),
    ("python", ["p", "y", "t", "h", "o", "n"], True),
])
def test_check_win_condition(secret, guessed, expected):
    assert check_win_condition(secret, guessed) == expected


def test_game_class_basic_flow():
    game = Game("apple")
    assert game.state == "ongoing"
    assert not game.is_game_over()
    
    game.play_turn("a")
    assert "a" in game.guessed_letters
    assert game.wrong_guesses == 0
    
    game.play_turn("z")
    assert game.wrong_guesses == 1


def test_game_win():
    game = Game("cat")
    game.play_turn("c")
    game.play_turn("a")
    game.play_turn("t")
    assert game.has_won()
    assert game.is_game_over()


def test_game_loss():
    game = Game("cat")
    for letter in "bdefghijklmnopqrsuvwxyz"[:6]:
        if not game.is_game_over():
            game.play_turn(letter)
    assert game.has_lost()

