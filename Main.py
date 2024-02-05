from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
import time




class Vvod():#Класс для работы с Tkinter
    def __init__(self, root): #Создание основного окна       
        root.title("Ввести")
        root.geometry("650x450")         
        login = Label(root, text = "Введите числа ")
        login.place(x = 30,y = 50)

        def buble_sort(chisla):#Функция сортировки пузырьком на вход принимает числа от пользователя
            start = time.thread_time()#Начало отсчета времение выполнения программы
            n=len(chisla)
            for i in range(n-1):
                for j in range(n-i-1):
                    if chisla[j] > chisla[j+1]:
                        chisla[j], chisla[j+1] = chisla[j+1], chisla[j]
            finish = time.thread_time()#Конец отсчета времение выполнения программы
            vrem = finish-start#Разница во времени между началом и концом = времени выполнения программы
            return(chisla,vrem)
        
        def vstoen(chisla):#Фунцкия сортировки встроенным методом
            start = time.thread_time()
            chisla=chisla.sort()
            finish = time.thread_time()
            vrem = finish-start
            return(chisla,vrem)
        
        def selection_sort(chisla):#Функция сортировки выборкой
            start = time.thread_time()    
            for i in range(len(chisla)):            
                lowest_value_index = i                
                for j in range(i + 1, len(chisla)):
                    if chisla[j] < chisla[lowest_value_index]:
                        lowest_value_index = j                
                chisla[i], chisla[lowest_value_index] = chisla[lowest_value_index], chisla[i]
            finish = time.thread_time()
            vrem = finish-start
            return(chisla,vrem)
        
        def heapify(chisla, heap_size, root_index):#Вспомогательная функция пирамидльной сортировки
            largest = root_index
            left_child = (2 * root_index) + 1
            right_child = (2 * root_index) + 2
            if left_child < heap_size and chisla[left_child] > chisla[largest]:
                largest = left_child
            if right_child < heap_size and chisla[right_child] > chisla[largest]:
                largest = right_child
            if largest != root_index:
                chisla[root_index], chisla[largest] = chisla[largest], chisla[root_index]            
                heapify(chisla, heap_size, largest)

        def heap_sort(chisla):#Основная функция пирамидальной сортировки 
            start = time.thread_time()     
            n = len(chisla)            
            for i in range(n, -1, -1):
                heapify(chisla, n, i)            
            for i in range(n - 1, 0, -1):
                chisla[i], chisla[0] = chisla[0], chisla[i]
                heapify(chisla, i, 0)
            finish = time.thread_time()
            vrem = finish-start
            return(chisla,vrem)
            
        def on_click_bubble():#Фунцкия кнопки при выборе метода сортировки пузырьком
            cifri = (cif.get()) 
            cifri = cifri.split(',')                
            res,vrem = buble_sort(cifri)
            itog_res ="Отсортированный массив " + str(res)+ " Потрачено времени "+str(vrem)
            result = Label(root, text = str(itog_res)) 
            result.place (x = 50,y = 100)
        def on_click_vstroen():#Фунцкия кнопки при выборе метода сортировки встроенной
            cifri = (cif.get()) 
            cifri = cifri.split(',')                
            res,vrem = vstoen(cifri)
            itog_res ="Отсортированный массив " + str(res)+ " Потрачено времени "+str(vrem)
            result = Label(root, text = str(itog_res)) 
            result.place (x = 50,y = 100)
        def on_click_selection():#Фунцкия кнопки при выборе метода сортировки выборкой
            cifri = (cif.get()) 
            cifri = cifri.split(',')                
            res,vrem = selection_sort(cifri)
            itog_res ="Отсортированный массив " + str(res)+ " Потрачено времени "+str(vrem)
            result = Label(root, text = str(itog_res)) 
            result.place (x = 50,y = 100)
        def on_click_heap():#Фунцкия кнопки при выборе метода пирамидальной сортировки
            cifri = (cif.get()) 
            cifri = cifri.split(',')                
            res,vrem = heap_sort(cifri)
            itog_res ="Отсортированный массив " + str(res)+ " Потрачено времени "+str(vrem)
            result = Label(root, text = str(itog_res)) 
            result.place (x = 50,y = 100)
 
        def selection(event):#Функция выборка действия из комбобокса Tkinter
            selection = combo.get()
            if selection == "Пузырьком":
                button = Button(root, text = "Ввести", command = on_click_bubble)
                button.place (x = 50,y = 260) 
            elif selection == "Встроенной":
                button = Button(root, text = "Ввести", command = on_click_vstroen)
                button.place (x = 50,y = 260) 
            elif selection == "Выборкой":
                button = Button(root, text = "Ввести", command = on_click_selection)
                button.place (x = 50,y = 260)
            elif selection == "Пирамидальная":
                button = Button(root, text = "Ввести", command = on_click_heap)
                button.place (x = 50,y = 260)


        for_combo = Label(root, text = "Выберите способ")
        for_combo.place(x = 350,y = 50) 
        sposob = ["Пузырьком", "Встроенной", "Выборкой" , "Пирамидальная"]
        combo = ttk.Combobox(values=sposob)
        combo.place(x = 500,y = 50)        
        combo.bind("<<ComboboxSelected>>", selection)
        cif = Entry(root, width=30, fg='blue', bg='aqua', borderwidth=3)      
        cif.place (x = 130,y = 50)
        
        
        
        
try:

    if __name__ == "__main__":
        root = tk.Tk()
        Vvod(root)    
        root.mainloop() 
except Exception:
    print('Попробуйте еще')
