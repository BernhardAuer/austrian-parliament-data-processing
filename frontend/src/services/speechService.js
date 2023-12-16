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

            // merge multiple consequtive paragraphs by same speaker & integrate time information (if available)
            return speeches.reduce(
                (mergedSpeeches, currentItem, i) => {
                    // ignore time objects by default
                    if (currentItem?.type == 1 && currentItem?.subtype == "time") {
                        return mergedSpeeches;
                    }
                    // first speach paragraph by any person
                    if (i == 0 || (speeches[i-1]?.nameOfSpeaker != currentItem?.nameOfSpeaker) ) {                        
                        // add time information if available
                        let previousItem = speeches[i-1];
                        if (previousItem?.type == 1 && previousItem?.subtype == "time") {
                            currentItem.time = previousItem?.data;
                        }

                        currentItem.data = currentItem?.data ? [currentItem.data] : [];
                        mergedSpeeches.push(currentItem);
                    } else { 
                        // merge paragraph by same person
                        mergedSpeeches[mergedSpeeches.length - 1]?.data.push(currentItem?.data);
                    }
                    return mergedSpeeches;
                },
                []
            );

        } catch (e) {
            console.log(e);
        }
        return null;
    }
}

