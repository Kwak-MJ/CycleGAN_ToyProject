I used CycleGAN for my toy project.

The project was inspired by an animation called Pokémon. We selected five types(fire, water, grass, ground, and electric) among lots of types in Pokémon and try to apply such types to people.
We experimented with CycleGAN as our first model, attracted by the availability of unparalleled image datasets.

When applying CycleGAN, our attempts were divided into two. The first was to use natural pictures of real fire, water, grass, electricity, and ground for training. 
The second was to use characters of Pokémon with similar designs among target types for training.

However, the results were not good. They reacted sensitively to the overall background and color because they did not use paired data.
Therefore, in the first experiment, there was a problem of changing the color of the entire photo, including the person. It was simply the color change.

Brief results are as follows, and you can see it in CycleGAN_result1_2types.zip. 
Experiments were conducted only on fire and electric (lighting) because the results were not good.

![0120_output_a](https://github.com/user-attachments/assets/010759ec-8dc3-466c-8be7-83e3ae356064)
![0120_input_b](https://github.com/user-attachments/assets/59bb3193-899f-41b4-9ff9-e42ea3e467d2)
![0324_output_a](https://github.com/user-attachments/assets/454fc64a-9990-42f4-934a-da3f11fb3159)
![0324_input_b](https://github.com/user-attachments/assets/fb4c82c3-aa32-4581-a233-475bebd8d49f)

In the second experiment, we learned with Pokémon pictures. The character has an image with the background.
Therefore, it was found that the characteristics inside the Pokémon boundary were reflected only to humans.

The results are shown in the picture below, and you can see more results in CycleGAN_result2_4types.zip.
Experiments were conducted only in four types: water, fire, grass, and electricity.

![0103_output_a](https://github.com/user-attachments/assets/bed416fa-9a69-4dfa-bfeb-b2b4955d78e0)
![0103_input_b](https://github.com/user-attachments/assets/f4355541-6a75-4e70-a791-66fbc149a4d7)

![0942_output_a](https://github.com/user-attachments/assets/dc7424d4-f498-431d-9b8e-5c42534a40bc)
![0942_input_b](https://github.com/user-attachments/assets/fa1a7acd-f2d9-4d3a-a511-99f7cc298142)

![0526_output_a](https://github.com/user-attachments/assets/920f4e6f-45bd-475b-841b-d37dbb84f808)
![0526_input_b](https://github.com/user-attachments/assets/5313ec68-ff30-48d7-a62b-fa0b85c8f8af)

![0286_output_a](https://github.com/user-attachments/assets/46a7914a-4006-4795-a4b8-862c71eebadf)
![0286_input_b](https://github.com/user-attachments/assets/870bd1c5-5372-4dc6-8cd3-841130d34c41)


However, our team thought that the goal was not to simply reflect colors on people. Therefore, after two experiments using CycleGAN, we decided to try a different model.


