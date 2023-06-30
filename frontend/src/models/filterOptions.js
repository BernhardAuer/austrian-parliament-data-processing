export default class FilterOptions {
    legislature = null;
    meetingNumber = null;
    topic = null;
    politicalParties = null;

	constructor(filterOptions) {
		if (filterOptions == null) {
			return;
		}
		this.legislature = filterOptions.legislature;
		this.meetingNumber = filterOptions.meetingNumber; 
		this.topic = filterOptions.topic;
		this.politicalParties = filterOptions.politicalParties;
	}

    get longNamesOfPoliticalParties() {
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
