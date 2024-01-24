import tkinter as tk
import requests
import json

url = "https://kitsu.io/api/edge/anime?filter[text]="


def anime_info():
    def anime_search(event):
        query = search_entry.get()
        raw_data = requests.get(url + query)
        data = raw_data.json()
        # вывод результатов
        size = len(data["data"])
        for i in range(size):
            results.insert(tk.END, str(i + 1) + " " + data["data"][i]["attributes"]["canonicalTitle"] + "\n")

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
    results = tk.Text(root, width=80, height=25)
    results.place(x=25, y=150)
    search_button.bind("<Button-1>", anime_search)
    root.mainloop()


if __name__ == '__main__':
    anime_info()
