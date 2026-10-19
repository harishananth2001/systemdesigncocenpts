7. Serialization — Converting data into a transferable format
Serialization converts an object or data structure into a format that can be transmitted or stored. Deserialization converts that representation back into a usable data structure.

Angular uses JavaScript objects. Django commonly uses Python objects and Django model instances. They need a shared format to exchange information.

<!-- check image -->


<!-- check code python ->angular ->python -->
This serializer specifies which fields appear in the serialized output.
Common formats
Format	Typical use
JSON	Common web API format
XML	Some legacy and enterprise integrations
Protocol Buffers	Compact, schema-based communication
MessagePack	Compact binary representation of structured data
JSON is a good default for your Angular + Django practice project.

Important: Serialization is not encryption. JSON is usually readable text. HTTPS/TLS protects data in transit, whereas serialization determines how the data is represented.

Interview question: Why do we use serializers in Django REST Framework?

They convert data into representations such as JSON and can validate incoming data before the application creates or updates database records.