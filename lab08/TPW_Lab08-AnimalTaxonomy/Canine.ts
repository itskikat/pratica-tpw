import Mammal from "./Mammal";

class Canine extends Mammal {

    static nCanines: number = 0;

    race: string;

    constructor(habitat: string, race: string){
        super(habitat);
        this.race = race;
        Canine.nCanines++;
    }

    show() {
        return super.show() + "\nRace: " + this.race;
    }

}

export default Canine;