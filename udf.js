function transform(line) {
    var values = line.split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/g);

    var obj = new Object();
    obj.id = values[0];
    obj.name = values[1];
    obj.supertype = values[2];
    obj.subtypes = values[3];
    obj.level = values[4];
    obj.hp = values[5];
    obj.types = values[6];
    obj.evolvesFrom = values[7];
    obj.abilities = values[8];
    obj.attacks = values[9];
    obj.weaknesses = values[10];
    obj.resistances = values[11];
    obj.retreatCost = values[12];
    obj.convertedRetreatCost = values[13];
    obj.set = values[14];
    obj.number = values[15];
    obj.artist = values[16];
    obj.rarity = values[17];
    obj.flavorText = values[18];
    obj.nationalPokedexNumbers = values[19];
    obj.legalities = values[20];
    obj.images = values[21];
    obj.tcgplayer = values[22];
    obj.cardmarket = values[23];
    obj.evolvesTo = values[24];
    obj.rules = values[25];
    obj.regulationMark = values[26];
    obj.ancientTrait = values[27];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
