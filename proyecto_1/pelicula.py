#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Pelicula():

    def __init__(self):
        self.__nombre = None
        self.__actores = []
        self.__genero = []
        self.__votos = None

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre

    def get_actores(self):
        return self.__actores

    def set_actores(self, actor):
        if isinstance(actor, str):
            self.__actores.append(actor)

    def get_votos(self):
        return self.__votos

    def set_votos(self, votos):
        if isinstance(votos, float):
            self.__votos = votos

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        if isinstance(genero, str):
            self.__genero.append(genero)
