def main():
    hero = input("Please Choose hero: V, Jack Sparrow or Batman:" )
    print(quotes[hero])
quotes = {
"V": "\"Everybody is a hero, a lover, a fool, a villain.\"",
"Jack Sparrow" : "\"The only rules that matter are these: what a man can do, and what a man can't do.\"",
"Batman" : "\"I am Vengeance\""
}
main()