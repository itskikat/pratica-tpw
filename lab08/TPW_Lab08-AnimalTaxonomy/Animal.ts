class Animal {

    static nAnimals: number = 0;

    habitat: string;

    constructor(h: string) {
        this.habitat = h;
        Animal.nAnimals++;
    }

    show() {
        return "Number of Animals: " + Animal.nAnimals + "\nHabitat: " + this.habitat;
    }
}

export default Animal;