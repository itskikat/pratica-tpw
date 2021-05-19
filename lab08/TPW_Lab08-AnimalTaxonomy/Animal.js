"use strict";
exports.__esModule = true;
var Animal = /** @class */ (function () {
    function Animal(h) {
        this.habitat = h;
        Animal.nAnimals++;
    }
    Animal.prototype.show = function () {
        return "Number of Animals: " + Animal.nAnimals + "\nHabitat: " + this.habitat;
    };
    Animal.nAnimals = 0;
    return Animal;
}());
exports["default"] = Animal;
