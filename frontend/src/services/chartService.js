import { ApiClient, SpeechesMetaDataApi } from './../javascript-client-generated/src/index.js';
import { env } from '$env/dynamic/public'

export default class ChartService {
	#apiInstance;
	constructor() {
		const client = new ApiClient();
		client.basePath = env.PUBLIC_API_URL;
		this.#apiInstance = new SpeechesMetaDataApi(client);
	}

	fetchSpeechTypes = async (selectedFilterOptions) => {
		let options = {
			legislature: selectedFilterOptions.legislature,
			meetingNumber: selectedFilterOptions.meetingNumber,
			topic: selectedFilterOptions.topic?.topic,
			politicalParty: selectedFilterOptions.politicalParties
		}

		let typeOfSpeechCountList = await this.#apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(options);

		let dataTemplate = {
			labels: [],
			datasets: [
				{
					data: [],
					backgroundColor: [],
					hoverBackgroundColor: []
				}
			]
		};

		if (!Array.isArray(typeOfSpeechCountList) && !typeOfSpeechCountList.length) {
			return dataTemplate;
		}

		dataTemplate.labels = Array.from(typeOfSpeechCountList, (element) => element.typeOfSpeech);
		dataTemplate.datasets[0].backgroundColor = Array.from(typeOfSpeechCountList, (element) => this.mapLabelsToBackgroundColor(element.typeOfSpeech));
		dataTemplate.datasets[0].hoverBackgroundColor = Array.from(typeOfSpeechCountList, (element) => this.mapLabelsToHoverColor(element.typeOfSpeech));
		dataTemplate.datasets[0].data = Array.from(typeOfSpeechCountList, (element) => element.count);

		return dataTemplate;
	}

	mapLabelsToBackgroundColor(labelName) {
		labelName = labelName.toLowerCase();
		let colorDict = {
			"contra": "#F7464A",
			"pro": "#68e08c",
			"erste lesung": "#949FB1",
			"regierungsbank": "#4D5360",
			"tatsächliche berichtigung": "#FDB45C",
			"ap": "#46BFBD",
			"aktuelle stunde": "#68bce0",
			"begründung": "#e068bc",
			"berichterstattung ausschuss": "#e08c68",
			"dringliche anfrage": "#e894c3",
			"dringlicher (entschließungs-)antrag": "#b994e8",
			"erklärung": "#94e8b9",
			"erwiderung": "#c3e894",
			"europäische union": "#df6a71",
			"wortmeldung zur geschäftsbehandlung": "#e89499",
			"kurze debatte": "#f6d3d5",
			"rf": "#7f85e3",
			"regierungsbank staatssekretär:in": "#d3d5f6",
			"regierungsvorlage": "#6adfd8",
			"unterzeichner:in": "#d3f6f3",
			"wahldebatte": "#df6a71",
			"wortmeldung": "#f1bec1",
		}
		return colorDict[labelName];
	}

	mapLabelsToHoverColor(labelName) {
		labelName = labelName.toLowerCase();
		let colorDict = {
			"contra": "#F7464A",
			"pro": "#68e08c",
			"erste lesung": "#949FB1",
			"regierungsbank": "#4D5360",
			"tatsächliche berichtigung": "#FDB45C",
			"ap": "#46BFBD",
			"aktuelle stunde": "#68bce0",
			"begründung": "#e068bc",
			"berichterstattung ausschuss": "#e08c68",
			"dringliche anfrage": "#e894c3",
			"dringlicher (entschließungs-)antrag": "#b994e8",
			"erklärung": "#94e8b9",
			"erwiderung": "#c3e894",
			"europäische union": "#df6a71",
			"wortmeldung zur geschäftsbehandlung": "#e89499",
			"kurze debatte": "#f6d3d5",
			"rf": "#7f85e3",
			"regierungsbank staatssekretär:in": "#d3d5f6",
			"regierungsvorlage": "#6adfd8",
			"unterzeichner:in": "#d3f6f3",
			"wahldebatte": "#df6a71",
			"wortmeldung": "#f1bec1",
		}
		return colorDict[labelName];
	}

	searchTopics = (searchTerm, legislature, meetingNumber) => {
		let options = {
			searchTerm: searchTerm,
			legislature: legislature,
			meetingNumber: meetingNumber
		}
		return this.#apiInstance.apiSpeechesMetaDataSearchTopicsGet(options);
	}

	getLegislaturesAndMeetings = () => {
		return this.#apiInstance.apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet();
	}

	mapPartiesToBackgroundColor(nameOfParty) {
		nameOfParty = nameOfParty.toLowerCase();
		let colorDict = {
			"v": "black",
			"s": "red",
			"f": "blue",
			"g": "green",
			"n": "pink"
		}
		return colorDict[nameOfParty];
	}

	getLongNameOfPoliticalParty = (shortName) => {
		let mapDict = {
			v: 'ÖVP',
			s: 'SPÖ',
			f: 'FPÖ',
			g: 'GRÜNE',
			n: 'NEOS'
		};
		let abbrToLower = shortName.toLowerCase();
		return mapDict[abbrToLower];
	};

	fetchSpeechDurations = async (selectedFilterOptions) => {
		let options = {
			legislature: selectedFilterOptions.legislature,
			meetingNumber: selectedFilterOptions.meetingNumber,
			topic: selectedFilterOptions.topic?.topic,
			politicalParty: selectedFilterOptions.politicalParties
		}

		let speechDurations = await this.#apiInstance.apiSpeechesMetaDataGetSpeechDurationsGet(options);
		let dataTemplate = {
			datasets: []
		};

		if (!Array.isArray(speechDurations) && !speechDurations.length) {
			return dataTemplate;
		}

		const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects
		let speechDurationsGroupedByParties = groupBy(speechDurations, (x) => x.politicalParty);

		for (let i = 0; i < Object.keys(speechDurationsGroupedByParties).length; i++) {
			let key = Object.keys(speechDurationsGroupedByParties)[i];
			let groupWithAdditionalProps = [];
			speechDurationsGroupedByParties[key].forEach(element => {
				let item = element;
				item.durationSumInMin = item.durationSumInSec / 60.0;
				groupWithAdditionalProps.push(item);
			});

			let chartDataGroup = { label: this.getLongNameOfPoliticalParty(key), data: groupWithAdditionalProps, backgroundColor: this.mapPartiesToBackgroundColor(key) };
			dataTemplate.datasets.push(chartDataGroup)
		}
		return dataTemplate;
	}

	fetchDistributionOfSpeakingTime = async (selectedFilterOptions) => {
		let options = {
			legislature: selectedFilterOptions.legislature,
			meetingNumber: selectedFilterOptions.meetingNumber,
			topic: selectedFilterOptions.topic?.topic,
			politicalParty: selectedFilterOptions.politicalParties
		}

		let speechDistribution = await this.#apiInstance.apiSpeechesMetaDataGetDistributionOfSpeakingTimeGet(options);
		let dataTemplate = {
			datasets: []
		};

		if (!Array.isArray(speechDistribution) && !speechDistribution.length) {
			return dataTemplate;
		}

		let chartDataSpeechDurationPercentage = {
			label: "Sprechdauer",
			data: speechDistribution.map(x => { return { y: x.speechDurationPercentage, x: this.getLongNameOfPoliticalParty(x.politicalParty) }; }),
			backgroundColor: speechDistribution.map(x => this.mapPartiesToBackgroundColor(x.politicalParty))
		};
		dataTemplate.datasets.push(chartDataSpeechDurationPercentage);

		let chartDataNumberOfSpeechesPercentage = {
			label: "Wortmeldungen",
			data: speechDistribution.map(x => { return { y: x.numberOfSpeechesPercentage, x: this.getLongNameOfPoliticalParty(x.politicalParty) }; }),
			backgroundColor: speechDistribution.map(x => this.mapPartiesToBackgroundColor(x.politicalParty))
		};
		dataTemplate.datasets.push(chartDataNumberOfSpeechesPercentage);

		return dataTemplate;
	}
}

