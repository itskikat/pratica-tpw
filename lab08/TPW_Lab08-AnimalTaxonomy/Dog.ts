import Canine from "./Canine";

class Dog extends Canine {

    static nDogs: number = 0;

    bark: string

    constructor(habitat: string, race: string, bark: string) {
        super(habitat, race);
        this.bark = bark;
        Dog.nDogs++;
    }

    talk() {
        return super.talk() + this.bark;
    }

}

export default Dog;