import { error } from '@sveltejs/kit';
import SpeechService from './../../../../../../services/speechService.js';
let service = new SpeechService();
let speechesByTopic = [];
let topics = [];
export const csr = false;

const groupBy = (x, f) => x.reduce((a, b, i) => ((a[f(b, i, x)] ||= []).push(b), a), {}); // credit: https://stackoverflow.com/questions/14446511/most-efficient-method-to-groupby-on-an-array-of-objects

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    let speech = await service.fetchPureSpeech({ legislature: params.legislature, meetingNumber: params.meetingNumber, topic: params.topic,
    speechNrInDebate: params.speechNrInDebate });    
    if (Array.isArray(speech) && !speech.length) {
        throw error(404, 'Not found');
    }


      
    return { speech
    };
}
