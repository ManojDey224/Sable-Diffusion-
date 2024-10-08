# -*- coding: utf-8 -*-
"""stable diffusion1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OGRsItzNW-0fzEejFKsvB07tLlrD2te6
"""

!pip install diffusers --upgrade
!pip install invisible_watermark transformers accelerate safetensors

import torch
import matplotlib.pyplot as plt
from diffusers import DiffusionPipeline, EulerDiscreteScheduler

!pip install pycuda

import pycuda.driver as cuda
import pycuda.autoinit

model_id = "stabilityai/stable-diffusion-2"

pipe = DiffusionPipeline.from_pretrained(model_id,
                                         torch_dtype=torch.float16,
                                         use_safetensors=True,
                                         variant="fp16")
pipe.to("cuda")

def generate_stable_diffusion_image(prompt):
    return pipe(prompt=prompt).images[0]

!pip install rich

import random
from rich.console import Console # import Console from rich.console
from rich.text import Text
import time

# Create a Console object

console = Console()

# List of random styles
styles = [
    "bold yellow on black",
    "bold white on blue",
    "bold magenta on green",
    "bold cyan on black",
    "bold red on white",
    "bold green on black",
    "bold blue on yellow",
    "bold black on magenta",
]
prompts = [
    "A breathtaking sunrise over the majestic Himalayas, where the first rays of sunlight illuminate the snow-capped peaks. Below, a lush valley shrouded in mist reveals terraced fields and small villages, with colorful prayer flags fluttering in the gentle breeze, symbolizing peace and spirituality.",
    "An enchanting underwater scene in the Great Barrier Reef, showcasing a vibrant coral ecosystem. Schools of tropical fish in brilliant hues swim among the corals, while a graceful sea turtle glides effortlessly through the crystal-clear water. Sunlight filters down from the surface, creating a magical atmosphere filled with life.",
    "A dense and thriving rainforest, where towering trees with thick canopies create a natural cathedral. Exotic birds with vivid plumage flit between branches, while colorful orchids and ferns blanket the forest floor. A serene waterfall cascades into a tranquil pool, surrounded by lush greenery and the sounds of nature.",
    "A futuristic cityscape at night, where sleek skyscrapers adorned with holographic advertisements rise against a starry sky. Flying cars zip through the air, leaving trails of light, while pedestrians walk along illuminated walkways. The city is a blend of nature and technology, with vertical gardens integrated into the architecture.",
    "An astronaut floating in the vastness of space, with Earth visible in the background, a vibrant blue and green marble against the black void. Stars twinkle in the distance, and a nearby satellite orbits silently. The astronaut's suit reflects the sunlight, creating a stunning contrast against the infinite cosmos.",
    "A close-up view of a high-tech computer circuit board, filled with intricate designs and glowing components. The board is alive with activity, showcasing data transmission through light pulses. This visual representation of technology highlights the complexity and beauty of modern electronics.",
    "A diverse group of people from various cultures gathered at a bustling street market, sharing a meal together. Colorful stalls display an array of dishes from around the world, with spices and aromas filling the air. Laughter and conversation blend as they enjoy traditional foods, celebrating unity in diversity.",
    "An artist passionately painting a large mural on a city wall, capturing the essence of urban life and cultural diversity. The mural features vibrant colors and intricate designs, depicting scenes of community, history, and hope. Bystanders watch in awe, inspired by the creativity and expression of the artist.",
    "A tranquil scene in a Japanese Zen garden, where a person practices mindfulness meditation. Surrounded by meticulously raked gravel, carefully placed rocks, and blooming cherry blossom trees, the individual finds peace and serenity. Soft petals fall gently around them, enhancing the atmosphere of calm.",
    "A majestic lion resting on a sunlit rock in the African savannah, its golden mane glistening in the warm light. The vast landscape stretches out behind it, dotted with acacia trees and distant mountains. This powerful creature embodies strength and grace, a true king of the wild.",
    "A playful dolphin leaping out of the ocean waves during a stunning sunset. The sky is painted in shades of orange, pink, and purple, reflecting on the water's surface. The dolphin's sleek body arcs gracefully through the air, capturing the joy and freedom of life in the sea.",
    "A close-up of a colorful butterfly perched delicately on a vibrant flower in a blooming garden. The intricate patterns on its wings are illuminated by sunlight, showcasing nature's artistry. Nearby, other insects buzz around, contributing to the lively atmosphere of the garden.",
    "A vast field of wildflowers in full bloom, showcasing a riot of colors—reds, yellows, blues, and purples. Bees and butterflies flit from flower to flower, pollinating as they go. In the distance, rolling hills provide a picturesque backdrop, creating a scene of natural beauty and harmony.",
    "A tranquil rice terrace in Bali, where lush green fields cascade down the hillside in a series of steps. Farmers work diligently, planting and harvesting rice, while the sun sets behind the mountains, casting a golden glow over the landscape. This image captures the beauty of agriculture and tradition.",
    "A stunning desert landscape featuring towering saguaro cacti under a starry night sky. The Milky Way stretches across the heavens, illuminating the desert floor with a soft glow. The cacti stand tall and proud, symbolizing resilience in the harsh environment.",
    "An abstract representation of emotions, using vibrant colors and fluid shapes to convey the complexity of human feelings. Swirls of reds, blues, and yellows blend together, creating a dynamic visual that captures joy, sadness, and tranquility in a single frame.",
    "A breathtaking view of the Grand Canyon at sunset, where the sun casts warm hues of orange and pink across the dramatic rock formations. The Colorado River winds through the canyon floor, reflecting the colors of the sky. This natural wonder showcases the beauty of the earth's geological history.",
    "A traditional Japanese temple surrounded by vibrant autumn foliage, with maple leaves in shades of red and gold falling gently to the ground. The temple's architecture is a stunning example of cultural heritage, harmonizing with the natural beauty of the changing seasons.",
    "A lively festival scene in Rio de Janeiro, filled with samba dancers in colorful costumes, vibrant decorations, and an energetic atmosphere. The streets are alive with music and laughter as people celebrate, showcasing the rich cultural heritage of Brazil.",
    "A panoramic view of the Northern Lights dancing over a snowy landscape in Iceland. The sky is illuminated with shades of green, purple, and blue, creating a magical display. In the foreground, a cozy cabin with smoke rising from the chimney adds warmth to the cold, pristine environment."
]
for prompt in prompts:
    print(prompt)

    # Randomly select a style from the styles list
    random_style = random.choice(styles)

    # Create highlighted text for the prompt with the random style
    highlighted_prompt = Text(prompt, style=random_style)

    # Print the highlighted prompt
    console.print(highlighted_prompt)

    # Generate the image
    img = generate_stable_diffusion_image(prompt)


    # Display the image
    if img is not None:
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()

    time.sleep(2)  # Wait for 2 seconds before showing the next image

prompts = [
    "A serene sunset over a tranquil lake, with vibrant orange and pink hues reflecting on the water, surrounded by lush green trees and distant mountains, in the style of a classic oil painting.",
    "A magical forest filled with colorful flowers and whimsical creatures, including fairies and butterflies, under a bright blue sky with fluffy white clouds, reminiscent of a children's storybook illustration.",
    "A snowy winter landscape, featuring a cozy cabin with smoke rising from the chimney, surrounded by tall pine trees and a frozen pond, illuminated by the soft glow of the moonlight.",
    "A playful puppy chasing butterflies in a sunny garden, with blooming flowers and a bright blue sky, capturing the joy of childhood and the innocence of pets.",
    "A majestic lion resting under a tree in the savannah, with golden grass swaying in the breeze and a vibrant sunset in the background, showcasing the beauty of wildlife.",
    "A colorful underwater scene with tropical fish and coral reefs, highlighting the diversity of marine life, with sunlight filtering through the water, creating a magical atmosphere.",
    "A whimsical castle in the clouds, surrounded by floating islands and rainbow-colored hot air balloons, evoking a sense of wonder and adventure, inspired by fairy tales.",
    "A friendly dragon playing with children in a meadow, with colorful flowers and butterflies, illustrating a scene of friendship and fantasy.",
    "An enchanted library filled with magical books and glowing orbs, where a young wizard is reading under a starry night sky, capturing the essence of imagination and learning.",
    "A group of children playing soccer in a park, with bright green grass, trees in the background, and a blue sky, showcasing the joy of outdoor activities and teamwork.",
    "A family having a picnic on a sunny day, with a checkered blanket, delicious food, and laughter, surrounded by nature, emphasizing the importance of family and togetherness.",
    "A cozy café scene with people enjoying coffee and pastries, featuring warm lighting, bookshelves, and a friendly barista, reflecting a sense of community and relaxation.",
    "A child painting at an easel in a sunny room, surrounded by colorful paints and brushes, capturing the creativity and joy of artistic expression.",
    "A vibrant art studio filled with various art supplies, where artists are working on different projects, showcasing the beauty of creativity and collaboration.",
    "A whimsical craft fair with booths displaying handmade items, featuring cheerful vendors and visitors, highlighting the charm of local artisans and creativity.",
    "A peaceful beach scene with children building sandcastles, seagulls flying overhead, and waves gently lapping at the shore, embodying the spirit of summer fun.",
    "An adorable baby elephant playing with a butterfly in a lush green jungle, symbolizing innocence and the beauty of nature.",
    "A group of friends camping under a starry sky, with a glowing campfire and tents, capturing the essence of adventure and friendship.",
    "A vibrant farmer's market filled with fresh fruits and vegetables, where families are shopping and enjoying the lively atmosphere.",
    "A colorful hot air balloon festival, with balloons of all shapes and sizes floating in the sky, creating a festive and joyful scene.",
    "A cheerful snowman wearing a scarf and hat, surrounded by children playing in the snow, illustrating the joy of winter activities.",
    "A magical treehouse nestled in the branches of a giant tree, with a rope ladder and fairy lights, inviting children to explore and play.",
    "A beautiful garden filled with blooming flowers and buzzing bees, showcasing the harmony of nature and the importance of pollinators.",
    "A futuristic city skyline at dusk, with flying cars and glowing buildings, capturing the imagination of what the future could hold.",
    "A cozy reading nook with a child curled up with a book, surrounded by soft pillows and warm lighting, promoting the love of reading.",
    "A vibrant carnival scene with colorful rides, games, and happy families enjoying the festivities, filled with laughter and excitement.",
    "A majestic whale swimming gracefully in the ocean, with sunlight streaming down through the water, highlighting the beauty of marine life.",
    "A whimsical tea party with stuffed animals and children, set in a colorful garden, capturing the essence of childhood imagination.",
    "A friendly robot helping children with their homework in a bright classroom, showcasing the positive impact of technology on learning.",
    "A picturesque village during autumn, with colorful leaves falling from trees and children playing in the leaves, celebrating the beauty of the season.",
    "A magical fairy garden with tiny houses and sparkling lights, inhabited by friendly fairies, creating a sense of wonder and enchantment.",
    "A joyful family celebrating a birthday party, with balloons, cake, and laughter, emphasizing the importance of family traditions.",
    "A charming bakery filled with delicious pastries and treats, with a friendly baker serving customers, illustrating the joy of food and community.",
    "A young scientist conducting an experiment in a colorful lab, surrounded by beakers and bubbling potions, promoting curiosity and learning.",
    "A tranquil Zen garden with a child meditating, surrounded by rocks, sand, and carefully placed plants, emphasizing peace and mindfulness.",
    "A vibrant street art scene, with artists painting murals on walls, showcasing the beauty of creativity and self-expression.",
    "A magical winter wonderland with twinkling lights, ice skating, and snow-covered trees, capturing the joy of the holiday season.",
    "A friendly alien visiting Earth, exploring a park filled with children playing, illustrating the theme of friendship across worlds.",
    "A colorful parade with floats, dancers, and musicians celebrating a cultural festival, showcasing diversity and community spirit.",
    "A child flying a kite on a windy day, with a bright blue sky and fluffy clouds, capturing the joy of outdoor play.",
    "A cozy family movie night with popcorn, blankets, and laughter, emphasizing the importance of spending quality time together.",
    "A vibrant coral reef teeming with colorful fish and marine life, showcasing the beauty and diversity of underwater ecosystems.",
    "A magical night sky filled with shooting stars and constellations, where children are lying on the grass, dreaming and making wishes.",
    "A friendly bear having a picnic with woodland animals, surrounded by trees and flowers, illustrating the beauty of friendship in nature.",
    "A child exploring a magical cave filled with glowing crystals and treasures, capturing the spirit of adventure and discovery.",
    "A whimsical playground with unique equipment, where children are laughing and playing, promoting the joy of outdoor activities.",
    "A peaceful sunset over rolling hills, with a winding river and wildflowers, creating a sense of tranquility and beauty in nature.",
    "A vibrant and colorful dragon parade, with dancers and musicians, celebrating culture and creativity in a festive atmosphere."
]

for prompt in prompts:
    print(prompt)

    # Randomly select a style from the styles list
    random_style = random.choice(styles)

    # Create highlighted text for the prompt with the random style
    highlighted_prompt = Text(prompt, style=random_style)

    # Print the highlighted prompt
    console.print(highlighted_prompt)

    # Generate the image
    img = generate_stable_diffusion_image(prompt)


    # Display the image
    if img is not None:
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()

    time.sleep(2)  # Wait for 2 seconds before showing the next image