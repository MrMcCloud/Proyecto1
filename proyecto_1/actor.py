#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Actor():

    def __init__(self):
        self.__nombre = None

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

