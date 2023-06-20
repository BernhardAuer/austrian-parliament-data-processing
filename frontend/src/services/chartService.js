import { ApiClient, SpeechesMetaDataApi } from './../javascript-client-generated/src/index.js';
import { env } from '$env/dynamic/public'

export default class ChartService {
    #apiInstance;
    constructor() {
        const client = new ApiClient();
        client.basePath = env.PUBLIC_API_URL;
        this.#apiInstance = new SpeechesMetaDataApi(client);
    }
    
    fetchSpeechTypes = (selectedLegislatur, selectedMeetingNumber, inputTopic, selectedPoliticalParties) => {
        let options = {
            legislature:selectedLegislatur,
            meetingNumber: selectedMeetingNumber,
            topic: inputTopic,
            politicalParty: selectedPoliticalParties
        }
        
        return this.#apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(options);
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

