#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:45:03 2020

@author: sayngku
"""
import unittest

from tasks.one import first_task
from tasks.two import second_task
from tasks.three import third_task
from tasks.four import fourth_task
from tasks.utils import remove_punctuation, char_counter, PUNCTUATIONS


class TestFirstTask(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            first_task('')

    def test_none(self):
        with self.assertRaises(TypeError):
            first_task(None)

    def test_one_word(self):
        test = 'word'
        result = first_task(test)
        self.assertEqual(test[0], result[0])
        self.assertEqual(test[-1], result[-1])
        self.assertNotEqual(test, result)
        self.assertEqual(char_counter(test), char_counter(result))

    def test_sentence(self):
        test = 'Twinkle, twinkle, little star, how I wonder what you are...'
        result = first_task(test)
        self.assertEqual(len(test), len(result))
        i=0
        while i<len(test):
            if (((test[i] in PUNCTUATIONS)
                or (result[i] in PUNCTUATIONS))):
                self.assertEqual(test[i], result[i])
            i+=1
        test_words=remove_punctuation(result).split()
        result_words=remove_punctuation(test).split()
        self.assertEqual(len(test_words), len(result_words))
        i=0
        while i < len(test_words):
            self.assertEqual(len(test_words[i]), len(result_words[i]))
            self.assertEqual(len(test_words[i][0]), len(result_words[i][0]))
            self.assertEqual(len(test_words[i][-1]), len(result_words[i][-1]))
            self.assertEqual(char_counter(test_words[i]), char_counter(result_words[i]))
            if len(test_words[i]) > 3:
                self.assertNotEqual(test_words[i], result_words[i])
            i+=1
        # Todo (lena): find a way to test each word of the result satisfies the function logic
        # self.assertEqual(test[0], result[0])
        # self.assertEqual(test[-1], result[-1])


class TestSecondTask(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            second_task('')

    def test_none(self):
        with self.assertRaises(TypeError):
            second_task(None)

    def test_one_word(self):
        test = 'word'
        result = second_task(test)
        self.assertNotEqual(test, result)
        self.assertEqual(char_counter(test), char_counter(result))

    def test_sentence(self):
        test = 'London Bridge is falling down, falling down, falling down.'
        result = second_task(test)
        self.assertEqual(len(test), len(result))
        i=0
        while i<len(test):
            if (((test[i] in PUNCTUATIONS)
                or (result[i] in PUNCTUATIONS))):
                self.assertEqual(test[i], result[i])
            i+=1
        test_words=remove_punctuation(result).split()
        result_words=remove_punctuation(test).split()
        self.assertEqual(len(test_words), len(result_words))
        i=0
        while i < len(test_words):
            self.assertEqual(len(test_words[i]), len(result_words[i]))
            self.assertEqual(char_counter(test_words[i]), char_counter(result_words[i]))
            if len(test_words[i]) > 1:
                self.assertNotEqual(test_words[i], result_words[i])
            i+=1


class TestThirdTask(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            third_task('', 1)

    def test_none(self):
        with self.assertRaises(TypeError):
            third_task(None, 1)

    def test_unvalid_number(self):
        with self.assertRaises(ValueError):
            third_task('word', -1)

    def test_none_number(self):
        with self.assertRaises(TypeError):
            third_task('word', None)

    def test_sentence(self):
        test = 'Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall...'
        n=1
        while n < 6: 
            result = third_task(test, n)
            self.assertEqual(len(test), len(result))
            i=0
            while i<len(test):
                if (((test[i] in PUNCTUATIONS)
                    or (result[i] in PUNCTUATIONS))):
                    self.assertEqual(test[i], result[i])
                i+=1
            test_words=remove_punctuation(result).split()
            result_words=remove_punctuation(test).split()
            self.assertEqual(len(test_words), len(result_words))
            i=0
            while i < len(test_words):
                self.assertEqual(len(test_words[i]), len(result_words[i]))
                self.assertEqual(char_counter(test_words[i]), char_counter(result_words[i]))
                if (len(test_words[i]) < n
                    and len(test_words[i]) >1 ):
                    self.assertNotEqual(test_words[i], result_words[i])
                i+=1
            n+=1

class TestFourthTask(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            fourth_task('')

    def test_none(self):
        with self.assertRaises(TypeError):
            fourth_task(None)

    def test_one_word(self):
        test = 'word'
        result = fourth_task(test)
        self.assertNotEqual(test, result)
        self.assertEqual(test.lower(), result.lower())

    def test_sentence(self):
        test = 'One, two, three, four, five, Once I caught a fish alive.'
        result = fourth_task(test)
        self.assertNotEqual(test, result)
        self.assertEqual(test.lower(), result.lower())

unittest.main()
