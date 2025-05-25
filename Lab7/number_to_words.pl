% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space

% Your program goes here

% Facts

% Base numbers (0 to 19)
num_word(0, 'zero').
num_word(1, 'one').
num_word(2, 'two').
num_word(3, 'three').
num_word(4, 'four').
num_word(5, 'five').
num_word(6, 'six').
num_word(7, 'seven').
num_word(8, 'eight').
num_word(9, 'nine').
num_word(10, 'ten').
num_word(11, 'eleven').
num_word(12, 'twelve').
num_word(13, 'thirteen').
num_word(14, 'fourteen').
num_word(15, 'fifteen').
num_word(16, 'sixteen').
num_word(17, 'seventeen').
num_word(18, 'eighteen').
num_word(19, 'nineteen').

% Tens (20, 30, ..., 90)
tens_word(20, 'twenty').
tens_word(30, 'thirty').
tens_word(40, 'forty').
tens_word(50, 'fifty').
tens_word(60, 'sixty').
tens_word(70, 'seventy').
tens_word(80, 'eighty').
tens_word(90, 'ninety').

% Main Rule: for converting an input number N into English words
to_words(N) :-
    N =< 1000,
    pos_neg(N, Sentence),
    format('~s', [Sentence]).


% Rules for number conversion

% Negative numbers
pos_neg(N, Sentence) :-
    N < 0,
    PosN is abs(N),
    number_to_words(PosN, WordList),
    atomic_list_concat(['minus' | WordList], ' ', Sentence), !.

% Positive numbers.
pos_neg(N, Sentence) :-
    N >= 0,
    number_to_words(N, Words),
    atomic_list_concat(Words, ' ', Sentence), !.

% Number less than 20.
number_to_words(N, [Word]) :-
    N < 20,
    num_word(N, Word), !.

% Number with only tens.
number_to_words(N, [TensWord]) :-
    N < 100,
    0 is N mod 10,
    tens_word(N, TensWord), !.

% Numbers that can be divided into tens and digits (e.g. 35 into 30 and 5)
number_to_words(N, [TensWord, UnitsWord]) :-
    N < 100,
    Tens is (N // 10) * 10,
    Units is N mod 10,
    tens_word(Tens, TensWord),
    num_word(Units, UnitsWord), !.

% Numbers that only have hundreds in it. (e.g. 400)
number_to_words(N, [HundredsWord, 'hundred']) :-
    N < 1000,
    0 is N mod 100,
    Hundreds is N // 100,
    num_word(Hundreds, HundredsWord), !.

% Numbers that have hundreds and (tens and/or units). (e.g. 256)
number_to_words(N, [HundredsWord, 'hundred' | Rest]) :-
    N < 1000,
    Hundreds is N // 100,
    Remainder is N mod 100,
    num_word(Hundreds, HundredsWord),
    number_to_words(Remainder, Rest), !.

number_to_words(1000, ['one', 'thousand']).

% Test cases: Copy the test cases into the terminal to see the result.
%?- to_words(-1).
%?- to_words(0).
%?- to_words(10).
%?- to_words(11).
%?- to_words(15).
%?- to_words(19).
%?- to_words(20).
%?- to_words(21).
%?- to_words(54).
%?- to_words(85).
%?- to_words(99).
%?- to_words(100).
%?- to_words(101).
%?- to_words(376).
%?- to_words(872).
%?- to_words(999).
%?- to_words(1000).
%?- to_words(1001).
