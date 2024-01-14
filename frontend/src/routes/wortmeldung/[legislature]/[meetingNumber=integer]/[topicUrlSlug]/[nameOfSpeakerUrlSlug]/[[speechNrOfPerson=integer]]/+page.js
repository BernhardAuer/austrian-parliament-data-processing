import { error } from '@sveltejs/kit';
import SpeechService from './../../../../../../../services/speechService.js';
let service = new SpeechService();

/** @type {import('./$types').PageLoad} */
export async function load({ params, url }) {
    let speechPromise = service.fetchPureSpeech({ legislature: params.legislature, meetingNumber: params.meetingNumber, topicUrlSlug: params.topicUrlSlug,
    nameOfSpeakerUrlSlug: params.nameOfSpeakerUrlSlug, speechNrOfPerson: params?.speechNrOfPerson });    
    
    let sourceLinksPromise = service.fetchSpeechSourceLinks({ legislature: params.legislature, meetingNumber: params.meetingNumber, topicUrlSlug: params.topicUrlSlug,
        nameOfSpeakerUrlSlug: params.nameOfSpeakerUrlSlug, speechNrOfPerson: params?.speechNrOfPerson });

    let [speech, sourceLinks] = await Promise.all([speechPromise, sourceLinksPromise]);
    if (speech == null) {
        throw error(404, 'Not found');
    }
    return {
        speech: speech,
        legislature: params.legislature, 
        meetingNumber: params.meetingNumber, 
        topic: sourceLinks.topic,
        nameOfSpeaker: sourceLinks.nameOfSpeaker,
        sourceLinks: sourceLinks
    };
}
