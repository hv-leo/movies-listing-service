from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_insert_one_movie():
    response = client.post(
        "/movies",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=[{"name": "Random Name",
              "director": "Random director",
               "writers": "",
               "stars": "",
               "user_reviews": 10,
               "critic_reviews": 10,
               "rating": 10}]
    )
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_insert_random_number_of_movies_greater_than_one():
    import random
    number_of_movies = random.randint(2, 10)
    json = []
    for n in range(number_of_movies + 1):
        json.append({"name": f"Random Name_{n}",
                     "director": "Random director",
                     "writers": "",
                     "stars": "",
                     "user_reviews": 10,
                     "critic_reviews": 10,
                     "rating": 10})
    response = client.post(
        "/movies",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=json
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_get_all_movies():
    client.delete("/movies",
                  headers={"accept": "application/json"}
    )
    client.post(
        "/movies",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=[{"name": "Random Name",
              "director": "Random director",
               "writers": "",
               "stars": "",
               "user_reviews": 10,
               "critic_reviews": 10,
               "rating": 10}]
    )

    response = client.get("/movies",
                          headers={"accept": "application/json"})
    assert response.status_code == 200
    assert response.json() == [{"name": "Random Name",
                                "director": "Random director",
                                "writers": "",
                                "stars": "",
                                "user_reviews": 10,
                                "critic_reviews": 10,
                                "rating": 10}]


def test_delete_all_movies():
    response = client.delete("/movies",
                             headers={"accept": "application/json"}
                             )

    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_delete_movie_that_doesnt_exist():
    response = client.delete(
        "/movies/movie_that_does_not_exist",
        headers={"accept": "application/json"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_delete_movie_that_exists():
    client.post(
        "/movies",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=[{"name": "new_movie",
              "director": "Random director",
               "writers": "",
               "stars": "",
               "user_reviews": 10,
               "critic_reviews": 10,
               "rating": 10}]
    )
    response = client.delete(
        "/movies/new_movie",
        headers={"accept": "application/json"}
    )
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_update_movie_details_of_movie_that_doesnt_exist():
    response = client.patch(
        "/movies/movie_that_does_not_exist",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={"director": "director update",
              "writers": "",
              "stars": "",
              "user_reviews": 10,
              "critic_reviews": 10,
              "rating": 10}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_update_movie_details_of_movie_that_exists():
    client.post(
        "/movies",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=[{"name": "new_movie",
              "director": "Random director",
               "writers": "",
               "stars": "",
               "user_reviews": 10,
               "critic_reviews": 10,
               "rating": 10}]
    )
    response = client.patch(
        "/movies/new_movie",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={"director": "director update",
              "writers": "",
              "stars": "",
              "user_reviews": 10,
              "critic_reviews": 10,
              "rating": 10}
    )
    assert response.status_code == 200
    assert response.json() == {"ok": True}

