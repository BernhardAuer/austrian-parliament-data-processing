export default class FilterOptions {
    legislature = null;
    meetingNumber = null;
    topic = null;
    politicalParties = null;

    get longNamesOfPoliticalParties() {
		if (this.politicalParties == null){return [];}
        let mapDict = {
			"v": "ÖVP",
			"s": "SPÖ",
			"f": "FPÖ",
			"g": "GRÜNE",
			"n": "NEOS"
		}
		return Array.from(this.politicalParties, (element) => {
			let abbrToLower = element.toLowerCase();
			return mapDict[abbrToLower];
		}).join(", ");
    }
}
