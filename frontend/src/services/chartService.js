import { ApiClient, SpeechesMetaDataApi } from './../javascript-client-generated/src/index.js';
import { env } from '$env/dynamic/public'

export default class ChartService {
    #apiInstance;
    constructor() {
        const client = new ApiClient();
        client.basePath = env.PUBLIC_API_URL;
        this.#apiInstance = new SpeechesMetaDataApi(client);
    }
    fetchSpeechTypes(selectedLegislatur, selectedMeetingNumber, inputTopic, selectedPoliticalParties, callback) {
        let options = {
            legislature:selectedLegislatur,
            meetingNumber: selectedMeetingNumber,
            topic: inputTopic,
            politicalParty: selectedPoliticalParties
        }
        console.log("wenigstens die scheisse soll funktionierne")
        this.#apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(options, (error, data, response) => {
            console.log("??")
            if (error) {
                console.error("api call failed.")
                console.error(error);
                return null;
            } else {
                console.log("api call sucess.")
                let parsedData = JSON.stringify(data)
                console.log('API called successfully. Returned data: ' + parsedData);
                callback(data);
            }
        });
    }


    async fetchSpeechMetaData(callback) {
        this.#apiInstance.apiSpeechesMetaDataGet((error, data, response) => {
            if (error) {
                console.error(error);
                return null;
            } else {
                let parsedData = JSON.stringify(data)
                console.log('API called successfully. Returned data: ' + parsedData);
                callback(parsedData);
            }
        });
    }

    searchTopics = (searchTerm, legislature, meetingNumber) => {
        let options = {
            searchTerm: searchTerm,
            legislature: legislature,
            meetingNumber: meetingNumber
        }
        return new Promise((resolve, reject) => {
            this.#apiInstance.apiSpeechesMetaDataSearchTopicsGet(options, (error, data, response) => {
            
                if (error) {
                    console.error("search topic api call failed.")
                    console.error(error);
                    reject(error);
                } else {
                    console.log("search topic api call success.")
                    let parsedData = JSON.stringify(data)
                    console.log('API called successfully. Returned data: ' + parsedData);
                    resolve(data);
                }
            });
        })
        
    }

    getLegislaturesAndMeetings = () => {
      
        return new Promise((resolve, reject) => {
            this.#apiInstance.apiSpeechesMetaDataGetLegislaturesAndMeetingNumbersGet((error, data, response) => {
            
                if (error) {
                    console.error("get legislatures and meetings api call failed.")
                    console.error(error);
                    reject(error);
                } else {
                    console.log("get legislatures and meetings api call success.")
                    let parsedData = JSON.stringify(data)
                    console.log('API called successfully. Returned data: ' + parsedData);
                    resolve(data);
                }
            });
        })
        
    }
}

