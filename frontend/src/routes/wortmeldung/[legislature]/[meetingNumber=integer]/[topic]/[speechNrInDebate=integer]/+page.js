import { error } from '@sveltejs/kit';
import SpeechService from './../../../../../../services/speechService.js';
let service = new SpeechService();
export const csr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params, url }) {
    let speechPromise = service.fetchPureSpeech({ legislature: params.legislature, meetingNumber: params.meetingNumber, topic: params.topic,
    speechNrInDebate: params.speechNrInDebate });    
    
    let sourceLinksPromise = service.fetchSpeechSourceLinks({ legislature: params.legislature, meetingNumber: params.meetingNumber, topic: params.topic,
        speechNrInDebate: params.speechNrInDebate });  

    let [speech, sourceLinks] = await Promise.all([speechPromise, sourceLinksPromise]);
    if (speech == null) {
        throw error(404, 'Not found');
    }
    return {
        speech: speech,
        legislature: params.legislature, 
        meetingNumber: params.meetingNumber, 
        topic: params.topic,
        nameOfSpeaker: url.searchParams.get('speaker'),
        sourceLinks: sourceLinks
    };
}
