/**
 *  Copyright 2015 SmartThings
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
 *  Big Turn OFF
 *
 *  Author: SmartThings
 */
definition(
    name: "Big Turn OFF",
    namespace: "smartthings",
    author: "SmartThings",
    description: "Turn your lights off when the SmartApp is tapped or activated",
    category: "Convenience",
    iconUrl: "https://s3.amazonaws.com/smartapp-icons/Meta/light_outlet.png",
    iconX2Url: "https://s3.amazonaws.com/smartapp-icons/Meta/light_outlet@2x.png"
)

preferences {
	section("When This switch is off") {
    
		input "switches", "capability.switch", multiple: true
	}
    section("Turn this switch on") {
    
		input "switcheson", "capability.switch", multiple: true
	}
}

def installed(){
	subscribe(switches, "switch.off", apphandler)
}

def updated()
{
	unsubscribe()
	installed()
}

def apphandler(evt) {
	log.debug "appTouch: $evt"
	switcheson?.on()
}