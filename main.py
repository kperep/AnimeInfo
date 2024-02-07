import tkinter as tk
import requests
import json

url = "https://kitsu.io/api/edge/anime?filter[text]="


def anime_info():
    def anime_search(event):
        def show_info():
            search = selected_item.get()
            select_anime = 0
            for i in range(size):
                if data["data"][i]["attributes"]["canonicalTitle"] == search:
                    select_anime = i
            for i in buttons:
                i.destroy()



        query = search_entry.get()
        raw_data = requests.get(url + query)
        data = raw_data.json()
        # вывод результатов
        size = len(data["data"])        # кол-во аниме в выдаче
        show = [data["data"][i]["attributes"]["canonicalTitle"] for i in range(size)]   # поисковая выдача
        delta = 0
        selected_item = tk.StringVar()
        buttons = []
        for item in show:
            item_btn = tk.Radiobutton(text=item, value=item, variable=selected_item)
            item_btn.place(x=75, y=150+delta)
            buttons.append(item_btn)
            delta += 30
        result_btn = tk.Button(root, text="Выдать информацию", command=show_info)
        result_btn.place(x=300, y=500)



    root = tk.Tk()
    root.title("Anime Info")
    root.geometry("700x700")
    # интерфейс
    main_label = tk.Label(root, text="Anime Info", font=("Comic Sans MS", 20))
    main_label.place(x=275, y=10)
    search_entry = tk.Entry(root, width=50)
    search_entry.place(x=75, y=80)
    search_button = tk.Button(root, text="Как-то так...", font=("Comic Sans MS", 15))
    search_button.place(x=425, y=67)
    search_button.bind("<Button-1>", anime_search)
    root.mainloop()


if __name__ == '__main__':
    anime_info()
