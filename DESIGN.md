**Developer**: Nalin
**Collaborator(s)**: Nalin

### ONLY INTEGERS:

- Define a method `only_integers` with one parameter.
- The parameter of the method is `self`of data type class object `Sentence`.
- Define an accumulator variable `integers_only`.
- Assign an empty list to the accumulator variable, `integers_only`.
- Define a local variable `sentece_list`.
- Use the `split` method on the instance variable `sentence.split`  which returns a list.
- Assing the returned list to the local variable `sentence_list`.
- Use the `for loop` to iterate through `sentence_list`.
    - Check every item in `sentence_list` to see if it is a digit or not using the `isdigit` method.
    - If the item is a digit add it to the list(accumulator variable) `integers_only`.
- Use the `.join` method to join the items in the list `integers_only`.
- Assign the joined list to the instance variable `self.sentence`.



### FILTER WORDS:

- Define a method `filter_words` with two  parametera.
- The parameters of the method are `self`of data type class object `Sentence` and `word_lst` od data type `List`.
- Define a local variable `sentece_list`.
- Use the `split` method on the instance variable `sentence.split`  which returns a list.
- Assing the returned list to the local variable `sentence_list`.
- Use the `for loop` to iterate through the list `sentence_list`.
    - Check every item in the `sentence_list`.
        - If the item is in `word_lst` remove the item from `sentence_list`.
- Use the `.join` method to join the items in the list `sentence_list`.
- Assign the joined list to the instance variable `self.sentence`.

