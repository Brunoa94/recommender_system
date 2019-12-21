#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:44:59 2019

@author: BrunoAfonso
"""

from ContentBasedAlgorithm import ContentBasedAlgorithm
from MovieLens import MovieLens
from CollaborativeUser import CollaborativeUser
from CollaborativeItem import CollaborativeItem

class RecommenderSystem:

    def __init__(self):
        self.RecommenderStart()

    def RecommenderStart(self):

        user_number = input("Introduza o seu numero de utilizador: ")
        recommender_method = input("""Qual o método de recomendação que deseja utilizar?
        1- Content-based
        2- Collaborative User-based
        3- Collaborative Item-based
        """)
        if(recommender_method == "1"):
            self.content_user = ContentBasedAlgorithm(int(user_number))
            self.content_user.recommend()
        elif(recommender_method == "2"):
            self.collaborative_user = CollaborativeUser(user_number)
            self.collaborative_user.recommend()
        elif(recommender_method == "3"):
            self.collaborative_item = CollaborativeItem(user_number)
            self.collaborative_item.recommend()
        else:
            print("Número de método inválido")

RecommenderSystem()
