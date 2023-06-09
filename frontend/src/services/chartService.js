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
			"ap" : "#46BFBD", 
			"aktuelle stunde" : "#68bce0",
			"begründung" : "#e068bc",
			"berichterstattung ausschuss" : "#e08c68", 
			"dringliche anfrage" : "#e894c3",
			"dringlicher (entschließungs-)antrag" : "#b994e8",
			"erklärung" : "#94e8b9", 
			"erwiderung" : "#c3e894",
			"europäische union" : "#df6a71",
			"wortmeldung zur geschäftsbehandlung": "#e89499",
			"kurze debatte" : "#f6d3d5",
			"rf" : "#7f85e3",  
			"regierungsbank staatssekretär:in" : "#d3d5f6",
			"regierungsvorlage" : "#6adfd8",
			"unterzeichner:in" : "#d3f6f3",
			"wahldebatte" : "#df6a71",
			"wortmeldung" : "#f1bec1",
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
			"ap" : "#46BFBD", 
			"aktuelle stunde" : "#68bce0",
			"begründung" : "#e068bc",
			"berichterstattung ausschuss" : "#e08c68", 
			"dringliche anfrage" : "#e894c3",
			"dringlicher (entschließungs-)antrag" : "#b994e8",
			"erklärung" : "#94e8b9", 
			"erwiderung" : "#c3e894",
			"europäische union" : "#df6a71",
			"wortmeldung zur geschäftsbehandlung": "#e89499",
			"kurze debatte" : "#f6d3d5",
			"rf" : "#7f85e3",  
			"regierungsbank staatssekretär:in" : "#d3d5f6",
			"regierungsvorlage" : "#6adfd8",
			"unterzeichner:in" : "#d3f6f3",
			"wahldebatte" : "#df6a71",
			"wortmeldung" : "#f1bec1",
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
}

