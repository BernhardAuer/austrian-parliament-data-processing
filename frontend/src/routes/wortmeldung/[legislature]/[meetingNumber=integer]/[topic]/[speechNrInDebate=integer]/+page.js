import { error } from '@sveltejs/kit';
import SpeechService from './../../../../../../services/speechService.js';
let service = new SpeechService();
export const csr = false;

const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects

/** @type {import('./$types').PageLoad} */
export async function load({ params, url }) {
    let speech = await service.fetchPureSpeech({ legislature: params.legislature, meetingNumber: params.meetingNumber, topic: params.topic,
    speechNrInDebate: params.speechNrInDebate });    
    if (speech == null) {
        throw error(404, 'Not found');
    }
    return {
        speech: speech,
        legislature: params.legislature, 
        meetingNumber: params.meetingNumber, 
        topic: params.topic,
        nameOfSpeaker: url.searchParams.get('speaker')
    };
}
