import tkinter as tk
import requests
import json
from PIL import Image, ImageTk

url = "https://kitsu.io/api/edge/anime?filter[text]="


def anime_info():
    def anime_search(event):
        def show_info():
            def text_wrap(text, size):
                all_text = list(text.split("\n"))
                result = ""
                for elem in all_text:
                    for i in range(len(elem) // size):
                        if elem[0] == " ":
                            result += elem[1:size]
                        else:
                            result += elem[:size]
                        counter = 0
                        while (size + counter < len(elem) - 1) and (elem[size + counter] != " "):
                            result += elem[size + counter]
                            counter += 1
                        result += "\n"
                        elem = elem[size + counter:]
                    result += elem + "\n"
                return result

            global poster
            search = selected_item.get()
            select_anime = 0
            for i in range(size):
                if data["data"][i]["attributes"]["canonicalTitle"] == search:
                    select_anime = i

            result_btn.place_forget()
            poster_url = data["data"][select_anime]["attributes"]["posterImage"]["small"]
            # скачиваем постер аниме
            response = requests.get(poster_url)
            with open("cash/poster.jpeg", "wb") as file:
                file.write(response.content)
            # изменяем картинку на форме
            poster_raw = Image.open("cash/poster.jpeg")
            poster = ImageTk.PhotoImage(poster_raw)
            poster_label.configure(image=poster)
            poster_label.place(x=25, y=125)
            for i in buttons:
                i.destroy()
            anime_title = tk.Label(root, text=text_wrap(data["data"][select_anime]["attributes"]["canonicalTitle"], 30), font=("Comic Sans MS", 20), justify=tk.LEFT)
            anime_title.place(x=350, y=130)
            anime_synopsis = tk.Label(root, text=text_wrap(data["data"][select_anime]["attributes"]["synopsis"], 55), font=("Comic Sans MS", 12), justify=tk.LEFT)
            anime_synopsis.place(x=325, y=250)

        query = search_entry.get()
        raw_data = requests.get(url + query)
        data = raw_data.json()
        poster_label.place_forget()
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
    root.geometry("800x800")
    # интерфейс
    main_label = tk.Label(root, text="Anime Info", font=("Comic Sans MS", 20))
    main_label.place(x=275, y=10)
    search_entry = tk.Entry(root, width=50)
    search_entry.place(x=75, y=80)
    search_button = tk.Button(root, text="Как-то так...", font=("Comic Sans MS", 15))
    search_button.place(x=425, y=67)

    # призрачный постер
    poster_raw = Image.open("cash/start.png")
    poster = ImageTk.PhotoImage(poster_raw)
    poster_label = tk.Label(root, image=poster)
    poster_label.place(x=25, y=125)
    poster_label.place_forget()

    search_button.bind("<Button-1>", anime_search)

    root.mainloop()


if __name__ == '__main__':
    anime_info()
