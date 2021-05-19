import Feline from "./Feline";

class Cat extends Feline {

    static nCats: number = 0;

    name: string;
    meow: string;

    constructor(habitat: string, family: string, meow: string, name: string) {
        super(habitat, family)
        this.meow = meow;
        this.name = name;
        Cat.nCats++;
    }

    talk() {
        return super.talk() + this.meow;
    }

    show() {
        return super.show() + "\nFamily: " + this.family + "\nName: " + this.name;
    }

}

export default Cat;