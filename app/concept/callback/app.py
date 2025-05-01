# LangChain provides a callback system that allows you to hook into the various stages of your LLM application. 
# This is useful for logging, monitoring, streaming, and other tasks.

# Event	            Event Trigger	                                Associated Method

# Chat model start	When a chat model starts	                    on_chat_model_start
# LLM start	        When a llm starts	                            on_llm_start
# LLM new token	    When an llm OR chat model emits a new token	    on_llm_new_token
# LLM ends	        When an llm OR chat model ends	                on_llm_end
# LLM errors	    When an llm OR chat model errors	            on_llm_error
# Chain start	    When a chain starts running	                    on_chain_start
# Chain end	        When a chain ends	                            on_chain_end
# Chain error	    When a chain errors	                            on_chain_error
# Tool start	    When a tool starts running	                    on_tool_start
# Tool end	        When a tool ends	                            on_tool_end
# Tool error	    When a tool errors	                            on_tool_error
# Agent action	    When an agent takes an action	                on_agent_action
# Agent finish	    When an agent ends	                            on_agent_finish
# Retriever start	When a retriever starts	                        on_retriever_start
# Retriever end	    When a retriever ends	                        on_retriever_end
# Retriever error	When a retriever errors	                        on_retriever_error
# Text	            When arbitrary text is run	                    on_text
# Retry	            When a retry event is run	                    on_retry