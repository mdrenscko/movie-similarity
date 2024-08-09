
# import spacy
import spacy

# This will return a Language object containing all components and data needed to process text.
nlp = spacy.load('en_core_web_md')


def next_movie(description):
    # open and load file contents
    movies = open("movies.txt", "r")
    # declare and initialize a list to store movie list split into movie title and description
    split_list = []

    # split movies into title and description and store in list
    for i in movies:
        split_list.append(i.split(':'))
        

    # get number of movies in text file
    count = len(split_list)
    # declare and initialize list to store similarity values
    similarity_list = []

    model_sentence = nlp(description)

    # iterate as many times as the number of movies in the text file
    for i in range(0, count):
        # check similarity between the movie description with the recently watched movie description
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))
        

    # get the maximum similarity value
    max_similarity = max(similarity_list)
    
    # get index of highest similarity value
    max_similarity_index = similarity_list.index(max_similarity)
    

    # return movie title similar to watched movie
    return split_list[max_similarity_index][0]
   
# movie description to comapare with
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# call function that gets the next movie description that is similar to the watched movie
print("Next Movie Recommended to Watch: " + next_movie(hulk_description))
