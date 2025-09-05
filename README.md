Task-1: CNN for image classification 
  * i have used tensorflow library to implement
  * i have choosed 2 conv layer and 2 dense layer got accuracy of 70% in validation i have used relu as activation function and categorical crossentropy as loss fucntion and adam optimizer.
  * i have tried with 3 conv layer with all other params being same the accuracy went up to 80%
  * then i tried using dropout in dense layers and the accuracy went up to 83%.

Task-2: RAG system
  * I have use ollama and gemma3: 1b param model to run locally on my laptop.
  * using llama index to parse the docs and creating index at runtime and passing it to the retriever and creating a query retriever engine. other basic chunk size and settigns are mentioned 
  * the problem i faced here is running model locally. i have worked on this using API call from LLM whcih are big model to run on my laptop locally. 
