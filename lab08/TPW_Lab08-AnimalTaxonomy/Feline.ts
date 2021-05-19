import Mammal from "./Mammal";

class Feline extends Mammal {

    static nFelines: number = 0;

    family: string;

    constructor(habitat: string, family: string){
        super(habitat);
        this.family = family;
        Feline.nFelines++;
    }

}

export default Feline;