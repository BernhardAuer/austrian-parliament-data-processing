import { ApiClient, SpeechesMetaDataApi } from './../javascript-client-generated/src/index.js';
import { env } from '$env/dynamic/public'

export default class SpeechService {
    #apiInstance;
    constructor() {
        const client = new ApiClient();
        client.basePath = env.PUBLIC_API_URL;
        this.#apiInstance = new SpeechesMetaDataApi(client);
    }

    fetchSpeeches = async (options) => {

        try {

            let speeches = await this.#apiInstance.apiSpeechesMetaDataGetSpeechesGet(options);
            return speeches;
        } catch (e) {
            console.log(e);
        }
        return null;
    }

    fetchPureSpeech = async (options) => {

        try {

            let speeches = await this.#apiInstance.apiSpeechesMetaDataGetPureSpeechesGet(options);

            let speechItemsForGui = [];
            let tempSpeechContainer = null;
            speeches.forEach(element => {

                switch (element.type) {
                    case 1:
                        if (element.data.length === 5) { // e.g. 12.56
                            element.type = "time";
                        } else {
                            element.type = "info";
                        }
                        break;
                    case 3:
                        element.type = "speech";
                        break;
                    default:
                        element.type = "unknown";
                        break;
                }

                // check if new visual item begins
                if (tempSpeechContainer != null && tempSpeechContainer?.type != element.type && tempSpeechContainer?.type != "time") {
                    speechItemsForGui.push(tempSpeechContainer);
                    tempSpeechContainer = null;
                }
                if (tempSpeechContainer != null && tempSpeechContainer.type == "speech" && tempSpeechContainer.nameOfSpeaker != element.nameOfSpeaker) {
                    speechItemsForGui.push(tempSpeechContainer);
                    tempSpeechContainer = null;
                }

                if (tempSpeechContainer == null) {
                    tempSpeechContainer = {
                        text: []
                    };
                }

                // info items
                if (element.type == "info") {
                    tempSpeechContainer.type = "info";
                    tempSpeechContainer.text.push(element.data);

                }

                // info items
                if (element.type == "time") {
                    // handle special time info items
                    tempSpeechContainer.type = "time";
                    tempSpeechContainer.startTime = element.data;

                }

                // speech by "current" person
                if (element.type == "speech") {
                    tempSpeechContainer.type = "speech";
                    tempSpeechContainer.nameOfSpeaker = element.nameOfSpeaker;
                    tempSpeechContainer.politicalRole = element.politicalRole;
                    tempSpeechContainer.subtype = element.subtype;
                    tempSpeechContainer.text.push(element.data);
                }
            });
            // push last element to array
            speechItemsForGui.push(tempSpeechContainer);
            tempSpeechContainer = null;
            return speechItemsForGui;
        } catch (e) {
            console.log(e);
        }
        return null;
    }
}

