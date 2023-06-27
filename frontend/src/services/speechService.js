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
        } catch(e) {
            console.log(e);
        }
        return null;
    }

}

