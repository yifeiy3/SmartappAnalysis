/**
 *  17355Hidden1
 *
 *  Copyright 2021 Eric Yang
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 *  in compliance with the License. You may obtain a copy of the License at:
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
 *  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License
 *  for the specific language governing permissions and limitations under the License.
 *
 */
definition(
    name: "17355Hidden1",
    namespace: "yifeiy3",
    author: "Eric Yang",
    description: "When app is clicked, ring smoke alarm\r\notherwise just a normal turn switch on",
    category: "",
    iconUrl: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience.png",
    iconX2Url: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience@2x.png",
    iconX3Url: "https://s3.amazonaws.com/smartapp-icons/Convenience/Cat-Convenience@2x.png")


preferences {
	section("Smoke Alarm for reference") {
		input "smokealarm", "capability.alarm", required:true
	}
    section("Turn on this light"){
    	input "switchon", "capability.switch", required:true
    }
    section("When this light is off"){
    	input "switchoff", "capability.switch", required:true
    }
    section("Addin this door for reference"){
    	input "Door", "capability.lock", required:true
    }
}

def installed() {
	log.debug "Installed with settings: ${settings}"
	initialize()
}

def updated() {
	log.debug "Updated with settings: ${settings}"

	unsubscribe()
	initialize()
}

def initialize() {
	subscribe(switchoff, "switch.off", appHandler)
    subscribe(app, touchHandler)
}

def appHandler(evt){
	switchon.on()
}

def touchHandler(evt){
	smokealarm.siren()
}
// TODO: implement event handlers