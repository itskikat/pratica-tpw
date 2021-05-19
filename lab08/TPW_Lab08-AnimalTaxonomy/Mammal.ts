import Animal from "./Animal";

class Mammal extends Animal {

    static nMammals: number = 0;

    constructor(habitat: string) {
        super(habitat);
        Mammal.nMammals++;
    }

    show() {
        return "Number of Mammals: " + Mammal.nMammals + "\nHabitat: " + this.habitat;
    }

    talk() {
        return "Mammal is talking ";
    }

}

export default Mammal;