package main

type Issue []struct {
	Body  string `json:"body"`
	ID    int64  `json:"id"`
	Title string `json:"title"`
	URL   string `json:"url"`
	User  struct {
		ID int64 `json:"id"`
	} `json:"user"`
}
