import Animal from "./Animal";
import Cat from "./Cat";
import Dog from "./Dog";


let animal1 = new Animal("Planet Earth");
console.log(animal1);
console.log("------------------------")
let dog = new Dog("Cozy Home", "Yorkshire Terrier", "Woof Woof");
console.log(dog);
console.log(dog.show());
console.log(dog.talk());
console.log("------------------------")
let cat = new Cat("Another Cozy Home", "Persian", "Meow Meow", "Kitty Kat");
console.log(cat);
console.log(cat.show());
console.log(cat.talk());
console.log("------------------------")
console.log(animal1.show());